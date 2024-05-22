import dataclasses
import logging
import time
import config
from enum import Enum

import binascii
from serial import Serial

logging.basicConfig(level=logging.DEBUG)


class PantoMessageType(Enum):
    SYNC = 0x00
    HEARTBEAT = 0x01
    BUFFER_CRITICAL = 0x02
    BUFFER_READY = 0x03
    PACKET_ACK = 0x04
    INVALID_PACKET_ID = 0x05
    INVALID_DATA = 0x06
    POSITION = 0x10
    DEBUG_LOG = 0x20

    SYNCK_ACK = 0x80
    HEARTBEAT_ACK = 0x81
    MOTOR = 0x90
    PID = 0x91
    SPEED = 0x92
    TRANSITION_ENDED = 0x93
    CREATE_OBSTACLE = 0xA0


@dataclasses.dataclass()
class PositionData:
    x1: int | float
    y1: int | float
    x2: int | float
    y2: int | float
    r1: int | float
    r2: int | float
    g_x1: int | float
    g_y1: int | float
    g_x2: int | float
    g_y2: int | float


class PantoProtocol:
    def __init__(self, serial: Serial, timeout=10):
        logging.debug(f"Initializing PantoProtocol with serial {serial} and timeout {timeout}")
        self.con: Serial = serial
        self.timeout = timeout
        self.messages_received: list[bytes] = []
        self.messages_sent: list[bytes] = []
        self.messages_to_sent: list[bytes] = []

    def handle_sync(self, body):
        self.messages_to_sent.append(bytes.fromhex("445080000000"))

    def handle_heartbeat(self, body):
        self.messages_to_sent.append(bytes.fromhex("445081000000"))

    def handle_debug(self, body):
        logging.info("received debug message:")
        logging.info(body)

    def handle_transition_ended(self, body):
        return

    def verify_header(self, header: bytes):
        if header != b'DP':
            raise ValueError('Invalid Panto protocol header', binascii.hexlify(header))

    def verify_position(self, position: PositionData):
        return True

    def handle_position(self, body):
        x_1 = int.from_bytes(body[:4], byteorder='big', signed=False)
        y_1 = int.from_bytes(body[4:8], byteorder='big', signed=False)
        r_1 = int.from_bytes(body[8:12], byteorder='big', signed=False)
        g_x1 = int.from_bytes(body[12:16], byteorder='big', signed=False)
        g_y1 = int.from_bytes(body[16:20], byteorder='big', signed=False)
        x_2 = int.from_bytes(body[20:24], byteorder='big', signed=False)
        y_2 = int.from_bytes(body[24:28], byteorder='big', signed=False)
        r_2 = int.from_bytes(body[28:32], byteorder='big', signed=False)
        g_x2 = int.from_bytes(body[32:36], byteorder='big', signed=False)
        g_y2 = int.from_bytes(body[36:40], byteorder='big', signed=False)

        self.verify_position(PositionData(x_1, y_1, x_2, y_2, r_1, r_2, g_x1, g_y1, g_x2, g_y2))

    def before_message(self):
        pass

    def run(self):
        try:
            # consume single bytes until messages align
            """
            somtimes flashing the esp fails and the esp is stuck in a boot loop
            https://esp32.com/viewtopic.php?t=23203
            The esp is then stuck in a boot loop showing these messages here over and over again
            
            1162 mmu set 00010000, pos 00010000
            1162 mmu set 00020000, pos 00020000
            1162 mmu set 00030000, pos 00030000
            1162 mmu set 00040000, pos 00040000
            """

            good_sequence = "DP".encode("ascii")
            good_sequence_idx = 0
            bad_sequence = "1162 mmu set".encode("ascii")
            bad_sequence_idx = 0

            num_bytes_lost = 0

            while num_bytes_lost < 100:
                _byte = self.con.read(1)
                if _byte == good_sequence[good_sequence_idx].to_bytes():
                    good_sequence_idx += 1
                else:
                    good_sequence_idx = 0

                if _byte == bad_sequence[bad_sequence_idx].to_bytes():
                    bad_sequence_idx += 1
                else:
                    bad_sequence_idx = 0
                if config.developer:
                    logging.info("Received byte: %s", _byte)

                if good_sequence_idx == len(good_sequence):
                    logging.info("Seeking found good sequence... consuming message than switching to protocol")
                    msg_type = self.con.read(size=1)
                    package_id = self.con.read(size=1)
                    message_size = self.con.read(size=2)
                    body = self.con.read(size=int.from_bytes(message_size, byteorder="big"))
                    logging.info("consumed message... switching to protocol")
                    logging.info(f"msgtype: {binascii.hexlify(msg_type)}")
                    logging.info(f"package_id: {binascii.hexlify(package_id)}")
                    logging.info(f"message_size: {binascii.hexlify(message_size)}")
                    logging.info(f"body: {binascii.hexlify(body)}")
                    break

                if bad_sequence_idx == len(bad_sequence):
                    raise ValueError("Bad sequence found - Stuck in a  boot loop")
            else:
                raise ValueError("No start sequence matched...")

            start_time = time.time()
            while (start_time + self.timeout) > time.time():
                self.before_message()
                for message in self.messages_to_sent:
                    self.con.write(message)
                    self.messages_sent.append(message)
                self.messages_to_sent = []

                header = self.con.read(size=2)
                self.verify_header(header)

                msg_type = self.con.read(size=1)
                msg_type_as_int = int.from_bytes(msg_type, byteorder='big', signed=False)

                package_id = self.con.read(size=1)

                message_size = self.con.read(size=2)

                body = self.con.read(size=int.from_bytes(message_size, byteorder="big"))

                if msg_type_as_int == PantoMessageType.SYNC.value:
                    self.handle_sync(body)
                elif msg_type_as_int == PantoMessageType.HEARTBEAT.value:
                    self.handle_heartbeat(body)
                elif msg_type_as_int == PantoMessageType.POSITION.value:
                    self.handle_position(body)
                elif msg_type_as_int == PantoMessageType.DEBUG_LOG.value:
                    self.handle_debug(body)
                elif msg_type_as_int == PantoMessageType.PACKET_ACK.value:
                    continue
                elif msg_type_as_int == PantoMessageType.TRANSITION_ENDED.value:
                    self.handle_transition_ended(body)
                elif msg_type_as_int == PantoMessageType.INVALID_DATA.value:
                    logging.debug(f"Received INVALID DATA packet")
                    if len(self.messages_sent) > 0:
                        logging.debug("last message sent")
                        logging.debug(binascii.hexlify(self.messages_sent[-1]))
                    else:
                        logging.debug(f"No messages sent before")
                else:
                    logging.debug(f"Unknown message type {msg_type}")
                    logging.debug(f"Message {binascii.hexlify(header + msg_type + package_id + message_size + body)}")
                self.messages_received.append(header + msg_type + package_id + message_size + body)

                for message in self.messages_to_sent:
                    self.con.write(message)
                    self.messages_sent.append(message)
                self.messages_to_sent = []

        except Exception as e:
            logging.error("run failed with exception:", e)
            logging.error(e)
            logging.error("previously received messages:")
            for message in self.messages_received:
                logging.error(message)
            raise e
