import logging
import time
import unittest
import util
import serial
import binascii


logging.basicConfig(level=logging.DEBUG)

class ProtocolTest(unittest.TestCase):
    con = None

    def setUp(self):
        util.upload_firmware("firmware/03 panto firmware/firmware")

        com = "/dev/cu.usbserial-0001"

        self.con = serial.Serial(com, baudrate=115200, timeout=5)

    def test_timeout_10min(self):
        timeout = 5 * 60
        start_time = time.time()
        while start_time + timeout > time.time():
            header = self.con.read(size=2)

            msg_type = self.con.read(size=1)

            package_id = self.con.read(size=1)

            message_size = self.con.read(size=2)

            body = self.con.read(size=int.from_bytes(message_size, byteorder="big"))

            if msg_type == bytes.fromhex("20"):
                logging.info("received debug message:")
                logging.info(body)

            elif msg_type == bytes.fromhex("00"):
                logging.info("receive sync")
                self.con.write(bytes.fromhex("445080000000"))
            elif msg_type == bytes.fromhex("01"):
                logging.info("receive heartbeat")
                self.con.write(bytes.fromhex("445081000000"))
            elif msg_type == bytes.fromhex("10"):
                logging.info("receive position")
                """
                4450     // magic number
                10       // message type: position
                00       // packet ID: not utilized
                0028     // payload length: 2 handles, 5 values each, 4 bytes each - 2*5*4 = 40 = 0x28
                FFFFFFFF // x position of first handle
                FFFFFFFF // y position of first handle
                FFFFFFFF // rotation of first handle
                FFFFFFFF // x position of first handle's god object
                FFFFFFFF // y position of first handle's god object
                FFFFFFFF // x position of second handle
                FFFFFFFF // y position of second handle
                FFFFFFFF // rotation of second handle
                FFFFFFFF // x position of second handle's god object
                FFFFFFFF // y position of second handle's god object
                """
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

                logging.info(f"{x_1} {y_1} {r_1} {g_x1} {g_y1} {x_2} {y_2} {r_2} {g_x2} {g_y2}")
            else:
                logging.warning(binascii.hexlify(header))
                logging.warning((binascii.hexlify(msg_type)))
                logging.warning(binascii.hexlify(package_id))
                logging.warning(binascii.hexlify(message_size))
                logging.warning(binascii.hexlify(body))
                self.assertTrue(False)
        print("done")

    def tearDown(self):
        self.con.close()

