import dataclasses
import logging
import time
from enum import Enum

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
    x1: int
    y1: int
    x2: int
    y2: int
    r1: int
    r2: int
    g_x1: int
    g_y1: int
    g_x2: int
    g_y2: int


class PantoProtocol:
    def __init__(self, serial: Serial, timeout=10):
        self.con: Serial = serial
        self.timeout = timeout
        self.messages_received = []

    def handle_sync(self, body):
        self.con.write(bytes.fromhex("445080000000"))

    def handle_heartbeat(self, body):
        self.con.write(bytes.fromhex("445081000000"))

    def handle_debug(self, body):
        logging.info("received debug message:")
        logging.info(body)

    def verify_header(self, header: bytes):
        return True

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

    def run(self):
        start_time = time.time()
        while start_time + self.timeout > time.time():
            header = self.con.read(size=2)
            self.verify_header(header)

            msg_type = self.con.read(size=1)

            package_id = self.con.read(size=1)

            message_size = self.con.read(size=2)

            body = self.con.read(size=int.from_bytes(message_size, byteorder="big"))

            if msg_type == PantoMessageType.SYNC:
                self.handle_sync(body)
            elif msg_type == PantoMessageType.HEARTBEAT:
                self.handle_heartbeat(body)
            elif msg_type == PantoMessageType.POSITION:
                self.handle_position(body)
            elif msg_type == PantoMessageType.DEBUG_LOG:
                self.handle_debug(body)

            self.messages_received.append(header + msg_type + package_id + message_size + body)
