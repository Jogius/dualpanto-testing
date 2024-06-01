import unittest

from utils import util
import config

class Basic(unittest.TestCase):
    def test_shows_up_as_serial(self):
        print("This test requires you to interact with dualpanto device and test it physically using test paper-jig.")
        print("Please check./physical_test/line wall/README.md")
        print("When you tested, please press Enter key.")
        self.assertIn(config.COM_PORT, util.serial_ports())

    def test_compile_firmware(self):
        res = util.compile_firmware('firmware/hello world')
        self.assertEqual(res, 0, msg='failed to compile firmware. please first check platformIO config and installation')

    def test_upload_firmware(self):
        res = util.upload_firmware('./firmware/hello world')
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

class Haptics(unittest.TestCase):

    def test_line_wall(self):
        res = util.upload_firmware("firmware/haptics/line wall/firmware", False)
        print("")
        print("==========================")
        print("===== TEST LINE WALL =====")
        print("==========================")
        print("")

        print("This test requires you to interact with dualpanto device and test it physically using test paper-jig.")
        print("Please check./physical_test/line wall/README.md")
        print("When you tested, please press Enter key.")

        print("")
        print("==========================")
        print("===== TEST LINE WALL =====")
        print("==========================")
        input()
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

    def test_force_field(self):
        res = util.upload_firmware("firmware/haptics/force field/firmware", False)
        print("")
        print("==========================")
        print("==== TEST FORCE FIELD ====")
        print("==========================")
        print("")

        print("This test requires you to interact with dualpanto device and test it physically using test paper-jig.")
        print("Please check./physical_test/line wall/README.md")
        print("When you tested, please press Enter key.")

        print("")
        print("==========================")
        print("==== TEST FORCE FIELD ====")
        print("==========================")
        print("")
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

    def test_BIS_week7_go(self):
        res = util.upload_firmware("firmware/haptics/BIS week7 God Object/firmware", False)
        print("")
        print("====================================")
        print("======= BIS WEEK7 GOD OBJECT =======")
        print("====================================")
        print("")

        print("This test requires you to interact with dualpanto device and test it physically.")
        print("Please check./BIS/")
        print("When you tested, please press Enter key.")

        print("")
        print("====================================")
        print("======= BIS WEEK7 GOD OBJECT =======")
        print("====================================")
        print("")
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')



class Kinematics(unittest.TestCase):
    def test_kinematics_sync(self):
        res = util.upload_firmware("firmware/haptics/kinematics/firmware", False)
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')

    def test_BIS_week7_kinematics(self):
        res = util.upload_firmware("firmware/haptics/BIS week7 Kinematics/firmware", False)
        print("")
        print("====================================")
        print("======= BIS WEEK7 KINEMATICS =======")
        print("====================================")
        print("")

        print("This test requires you to interact with dualpanto device and test it physically")
        print("Please check./BIS/BIS.md")

        print("")
        print("====================================")
        print("======= BIS WEEK7 KINEMATICS =======")
        print("====================================")
        print("")
        self.assertEqual(res, 0, msg='failed to upload firmware. please first check platformIO config and installation')


class UploadDualPantoFramework(unittest.TestCase):
    def test_upload_dp_firmware(self):
        res = util.compile_firmware('firmware/dualpantoframework')
        self.assertEqual(res, 0, msg='failed to compile firmware. please first check platformIO config and installation')



class UploadDualPantoEncoderTest(unittest.TestCase):
    def test_upload_dp_encoder_test(self):
        res = util.compile_firmware('firmware/encoder_driver')
        self.assertEqual(res, 0, msg='failed to compile firmware. please first check platformIO config and installation')
