import unittest

from utils import util
import config

class Basic(unittest.TestCase):
    def test_shows_up_as_serial(self):
        self.assertIn(config.COM_PORT, util.serial_ports())

    def test_compile_firmware(self):
        res = util.compile_firmware('firmware/01 hello world')
        self.assertEqual(res, 0, msg='failed to compile firmware. please first check platformIO config and installation')

    def test_upload_firmware(self):
        res = util.upload_firmware('./firmware/01 hello world')
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')


class Haptics(unittest.TestCase):
    def test_shows_up_as_serial(self):
        self.assertIn(config.COM_PORT, util.serial_ports())

    def test_line_wall(self):
        res = util.upload_firmware("firmware/09 god object/firmware", False)
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

class Kinematics(unittest.TestCase):
    def test_forward(self):
        self.assertIn(config.COM_PORT, util.serial_ports())

    def test_inverse(self):
        self.assertIn(config.COM_PORT, util.serial_ports())