import logging
import unittest

import math
from parameterized import parameterized

from utils import util
import serial

import config

from utils.panto_protocol import PantoProtocol, PositionData

logging.basicConfig(level=logging.DEBUG)


class StrictPantoProtocol(PantoProtocol):
    def verify_position(self, position: PositionData):
        if position.g_x1 != 0:
            raise AssertionError('Invalid position data')
        if position.g_y1 != 0:
            raise AssertionError('Invalid position data')
        if position.g_x2 != 0:
            raise AssertionError('Invalid position data')
        if position.g_y2 != 0:
            raise AssertionError('Invalid position data')


class ReadEncoderProtocol(PantoProtocol):

    def __init__(self, con, timeout):
        super(ReadEncoderProtocol, self).__init__(con, timeout)
        self.positions = []

    def verify_position(self, position: PositionData):
        logging.info(f"{position.x1}, {position.y1}")
        self.positions.append(position)

    """
    returns the orientation of the handle in radians [0 - 2pi] 
    """

    def panto_to_unity_rotation(self, rotation: int) -> float:
        return rotation % 360 / (180 / math.pi)

    def panto_to_unity_position_x(self, pos: int):
        return pos / 10

    def panto_to_unity_position_z(self, pos: int):
        return pos / 10

    def panto_to_unity_position(self, position: PositionData):
        if position is None:
            return None
        return PositionData(
            self.panto_to_unity_position_x(position.x1),
            self.panto_to_unity_position_z(position.y1),
            self.panto_to_unity_position_x(position.x2),
            self.panto_to_unity_position_z(position.y2),
            self.panto_to_unity_rotation(position.r1),
            self.panto_to_unity_rotation(position.r2),
            self.panto_to_unity_position_x(position.x1),
            self.panto_to_unity_position_z(position.y1),
            self.panto_to_unity_position_x(position.x2),
            self.panto_to_unity_position_z(position.y2),
        )


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

    def verify_position(self, position: PositionData):
        pos = self.positions[self.position_index]
        if position.g_x1 != pos[0] or position.g_y1 != pos[1]:
            logging.warning(
                f'Invalid god position, expected {pos[0]} {pos[1]} received {position.g_x1} {position.g_y1}')

    def before_message(self):
        if len(self.messages_received) > 100 and len(self.messages_received) % 25 == 0:
            self.position_index += 1
            self.position_index %= len(self.positions)
            position = self.positions[self.position_index]
            x_g = position[0]
            y_g = position[1]
            rotation = 0

            x_bytes = x_g.to_bytes(4, byteorder='big')
            y_bytes = y_g.to_bytes(4, byteorder='big')
            r_bytes = rotation.to_bytes(4, byteorder='big')

            self.messages_to_sent.append(bytes.fromhex("44 50 90 00 00 0E 00 01") + x_bytes + y_bytes + r_bytes)


class ObstacleProtocol(PantoProtocol):
    def __init__(self, port, timeout):
        super(ObstacleProtocol, self).__init__(port, timeout)
        self.num_obstacles = 1

    def before_message(self):
        if len(self.messages_received) % 25 == 0 and 1 < len(self.messages_received) < 25 * 100:
            x1_bytes = (0).to_bytes(4, byteorder='big')
            y1_bytes = (0).to_bytes(4, byteorder='big')
            x2_bytes = (10).to_bytes(4, byteorder='big')
            y2_bytes = (10).to_bytes(4, byteorder='big')

            pkg_index = self.num_obstacles.to_bytes(1, byteorder='big')
            obstacle_id_bytes = self.num_obstacles.to_bytes(2, byteorder='big')

            self.num_obstacles += 1

            length_bytes = (1 + 2 + 4 * 4).to_bytes(2, byteorder='big')

            panto_index = (255).to_bytes(1, byteorder='big')

            self.messages_to_sent.append(bytes.fromhex("44 50 A0") + pkg_index + length_bytes + panto_index
                                         + obstacle_id_bytes + x1_bytes + y1_bytes + x2_bytes + y2_bytes)


class BaseProtocolTest(unittest.TestCase):
    con = None

    def setUp(self):
        if config.uploading_firmware:
            util.upload_firmware("firmware/dualpantoframework/firmware", False)
        com = config.COM_PORT
        self.con = serial.Serial(com, baudrate=115200, timeout=5)

    def tearDown(self):
        self.con.close()


class TestPantoProtocol(BaseProtocolTest):
    def test_timeout_1min(self):
        pp = StrictPantoProtocol(self.con, timeout=10)
        pp.run()

    def test_message_count(self):
        pp = StrictPantoProtocol(self.con, timeout=60)
        pp.run()
        self.assertTrue(len(pp.messages_received) > 100)

    def test_set_god_object(self):
        pp = GodobjectMovingProtocol(self.con, timeout=60)
        pp.run()
        self.assertTrue(len(pp.messages_received) > 100)

    def test_set_obstacle(self):
        pp = ObstacleProtocol(self.con, timeout=60)
        pp.run()
        self.assertTrue(len(pp.messages_received) > 100)
        self.assertTrue(pp.num_obstacles > 5)


class MovePantoManuallyTest(BaseProtocolTest):
    @parameterized.expand(
        [
            [
                "upper pantograph move y",
                "move",
                "upper pantograph",
                lambda x: x.y1,
                "1cm in Y direction",
                10
            ],
            [
                "upper pantograph move x",
                "move",
                "upper pantograph",
                lambda x: x.x1,
                "1cm in X direction",
                10
            ],
            [
                "lower pantograph move y",
                "move",
                "lower pantograph",
                lambda x: x.y2,
                "1cm in Y direction",
                10
            ],
            [
                "lower pantograph move x",
                "move",
                "lower pantograph",
                lambda x: x.x2,
                "1cm in X direction",
                10
            ],
            [
                "upper handle rotation",
                "rotate",
                "upper handle",
                lambda x: x.r1,
                "15 degrees",
                10 * math.pi / 180
            ],
            [
                "lower handle rotation",
                "rotate",
                "lower handle",
                lambda x: x.r2,
                "15 degrees",
                10 * math.pi / 180
            ]
        ]
    )
    def test_read_encoder(self, name, verb, dimension, extraction_function, move_thresh_str, move_thresh):
        print("---- this test needs manual input -----")
        input(f"please press enter and THEN {verb} the {dimension} by more than {move_thresh_str}")
        pp = ReadEncoderProtocol(self.con, timeout=1)
        pp.run()
        pos_start = extraction_function(pp.panto_to_unity_position(pp.positions[0]))
        pos_end = extraction_function(pp.panto_to_unity_position(pp.positions[-1]))
        logging.info(f"starting: {pos_start}")
        logging.info(f"ending: {pos_end}")
        print(f"registered a move of {abs(pos_start - pos_end)}")
        self.assertTrue(abs(pos_start - pos_end) > move_thresh)

    def test_read_encoder_live(self):
        pp = ReadEncoderProtocol(self.con, timeout=60)
        pp.run()