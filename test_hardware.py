import time
import unittest

from threading import Thread
import os

import serial

import util
import config


class HardwareTest(unittest.TestCase):
    encoder_pos = [0, 0, 0, 0]
    continue_serial_connection_flag = True

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
        res = util.upload_firmware('./firmware/03 motor')
        self.assertEqual(res, 0, msg='failed to upload firmware')
        time.sleep(1)
        print("Press any key to continue")
        input()

    def handle_serial_connection(self):
        print("Connecting...")
        with serial.Serial(config.COM_PORT, 9600, timeout=1, parity=serial.PARITY_EVEN) as ser:
            time.sleep(1)
            self.assertNotEqual(ser.inWaiting(), 0, msg="could not establish serial connection... try restarting the panto")
            uint_overflow_correction = [0,0,0,0]
            while self.continue_serial_connection_flag:
                if ser.inWaiting() > 0:
                    r = str(ser.readline()).split("dptest")
                    if len(r) != 2:
                        print(r, " has wrong serial format - skipping")
                        continue
                    new_encoder_pos = [int(y) for y in [x.split(",")[:-1] for x in r][1]]
                    print(new_encoder_pos)
                    # correcting the uint overflow -> 16383 (14bit max) jump to 0
                    for i in range(4):
                        if self.encoder_pos[i] -uint_overflow_correction[i] - new_encoder_pos[i] > 10000:
                            uint_overflow_correction[i] += 16383
                        if self.encoder_pos[i] - uint_overflow_correction[i] - new_encoder_pos[i] < -10000:
                            uint_overflow_correction[i] -= 16383
                        new_encoder_pos[i] += uint_overflow_correction[i]
                    for i in range(4, 6):
                        # 136 steps for the endeffector encoders
                        new_encoder_pos[i] = abs(new_encoder_pos[i] % (136 * 2))
                    self.encoder_pos = new_encoder_pos
                    #print(self.encoder_pos)
                else:
                    time.sleep(0.01)

    def test_encoder(self):
        #res = util.upload_firmware('./firmware/04 encoder read')
        #self.assertEqual(res, 0, msg='failed to upload firmware')
        time.sleep(1)
        # move serial connection handling to other thread
        serial_connection_thread = Thread(target=self.handle_serial_connection)
        serial_connection_thread.start()

        time.sleep(3)
        #self.assertEqual(len(self.encoder_pos), 4, msg="getting no data from connection thread")
        start_position = self.encoder_pos
        
        display_interval = 7500
        display_step_size = 200

        try: 
            while serial_connection_thread.is_alive():
                rel_pos = [self.encoder_pos[i] - start_position[i] for i in range(len(self.encoder_pos))]
                print("Move the handles to test the encoders")
                print(rel_pos)
                print(" " * int(display_interval / display_step_size), "|")
                for j in range(4): # four main encoders
                    b = True
                    for i in range(-display_interval, display_interval, display_step_size):
                        if rel_pos[j] < i and b:
                            b = False
                            print("#", end="")
                        else:
                            print(" ", end="")
                    if b:
                        print("#", end="")
                    print()
                print()
                for j in range(4, 6): # two endeffector encoders
                    print("#" * (rel_pos[j] // 2))
                print()
                print("Press CTRL + C to continue")
                time.sleep(0.05)
                os.system('cls' if os.name == 'nt' else 'clear')
        except KeyboardInterrupt:
            self.continue_serial_connection_flag = False

    def test_sync(self):
        res = util.upload_firmware('./firmware/05 move handles in sync')
        self.assertEqual(res, 0, msg='failed to upload firmware')
        time.sleep(1)
        with serial.Serial(config.COM_PORT, 9600, timeout=1) as ser:
            while True:
                message = b'dpmotor100234;'
                ser.write(message)
                #res = ser.read(1)
                #print(res)
               



if __name__ == "__main__":
    h = HardwareTest()
    #h.test_encoder()
    #h.test_motor()
    h.test_sync()