import time
import unittest

import serial

import util
import config


class HardwareTest(unittest.TestCase):
    def test_shows_up_as_serial(self):
        self.assertIn(config.COM_PORT, util.serial_ports())

    def test_compile_firmware(self):
        res = util.compile_firmware('firmware/01 hello world')
        self.assertEqual(res, 0)

    def test_upload_firmware(self):
        res = util.upload_firmware('./firmware/01 hello world')
        self.assertEqual(res, 0)

    def test_upload_firmware_check_serial(self):
        res = util.upload_firmware('./firmware/02 echo')
        self.assertEqual(res, 0, msg='failed to upload firmware')
        time.sleep(1)
        with serial.Serial(config.COM_PORT, 9600, timeout=1) as ser:
            message = b'x'
            ser.write(message)
            res = ser.read(1)
            self.assertEqual(res, message)


    def test_motor(self):
        # TODO
        ...

    def test_encoder(self):
        # TODO
        ...
