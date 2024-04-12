import unittest

import binascii

import util
import serial

from panto_protocol import PantoProtocol, PositionData


class StrictPantoProtocol(PantoProtocol):
    def verify_header(self, header: bytes):
        if header != b'DP':
            raise AssertionError('Invalid Panto protocol header')

    def verify_position(self, position: PositionData):
        if position.g_x1 != 0:
            raise AssertionError('Invalid position data')
        if position.g_y1 != 0:
            raise AssertionError('Invalid position data')
        if position.g_x2 != 0:
            raise AssertionError('Invalid position data')
        if position.g_y2 != 0:
            raise AssertionError('Invalid position data')


class GodobjectMovingProtocol(PantoProtocol):
    def __init__(self, port, timeout):
        super(GodobjectMovingProtocol, self).__init__(port, timeout)
        self.positions = [
            (0, 0),
            (10, 0),
            (10, 10),
            (0, 10)
        ]
        self.position_index = 0

    def verify_header(self, header: bytes):
        if header != b'DP':
            raise AssertionError('Invalid Panto protocol header', binascii.hexlify(header))

    def verify_position(self, position: PositionData):
        pos = self.positions[self.position_index]
        if position.g_x1 != pos[0] or position.g_y1 != pos[1]:
            raise AssertionError('Invalid position data, expected ', pos, 'received ', position)

    def before_message(self):
        if len(self.messages_received) > 25 and len(self.messages_received) % 25 == 0:
            self.position_index += 1
            self.position_index %= len(self.positions)
            position = self.positions[self.position_index]
            x_g = position[0]
            y_g = position[1]
            rotation = 0

            x_bytes = x_g.to_bytes(4, byteorder='big')
            y_bytes = y_g.to_bytes(4, byteorder='big')
            r_bytes = rotation.to_bytes(4, byteorder='big')

            self.con.write(bytes.fromhex("45 50 90 00 00 0E 00 01") + x_bytes + y_bytes + r_bytes)


class ProtocolTest(unittest.TestCase):
    con = None

    def setUp(self):
        util.upload_firmware("firmware/10 panto firmware/firmware", False)

        com = "/dev/cu.usbserial-0001"
        self.con = serial.Serial(com, baudrate=115200, timeout=5)

    def test_timeout_1min(self):
        pp = StrictPantoProtocol(self.con, timeout=60)
        pp.run()

    def test_message_count(self):
        pp = StrictPantoProtocol(self.con, timeout=60)
        pp.run()
        self.assertTrue(len(pp.messages_received) > 10)

    def test_set_god_object(self):
        pp = GodobjectMovingProtocol(self.con, timeout=60)
        pp.run()
        print()

    def tearDown(self):
        self.con.close()
