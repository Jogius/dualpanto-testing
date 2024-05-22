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

class Upload(unittest.TestCase):
    def test_upload_dp(self):
        res = util.upload_firmware("firmware/10 panto firmware/firmware", False)
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

    # def test_upload_firmware_check_serial(self):
    #     res = util.upload_firmware('./firmware/02 echo')
    #     self.assertEqual(res, 0, msg='failed to upload firmware')
    #     time.sleep(1)
    #     with serial.Serial(config.COM_PORT, 9600, timeout=1) as ser:
    #         message = b'x'
    #         ser.write(message)
    #         res = ser.read(1)
    #         self.assertEqual(res, message)

class Haptics(unittest.TestCase):
    def test_shows_up_as_serial(self):
        self.assertIn(config.COM_PORT, util.serial_ports())