import subprocess

import sys
import glob
import serial

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque

""" Lists serial port names

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
"""


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def compile_firmware(firmware_directory="./firmware/00 template", cleanup=True):
    res = subprocess.call('pio run', cwd=firmware_directory, shell=True)
    if cleanup:
        res += subprocess.call('pio run --target clean', cwd=firmware_directory, shell=True)
    return res


def upload_firmware(firmware_directory="./firmware/00 template", cleanup=True):
    res = subprocess.call('pio run', cwd=firmware_directory, shell=True)
    res += subprocess.call('pio run --target upload', cwd=firmware_directory, shell=True)
    if cleanup:
        res += subprocess.call('pio run --target clean', cwd=firmware_directory, shell=True)
    return res


class AnalogPlot:
    # constr
    def __init__(self, strPort, maxLen):
        # open serial port
        self.ser = serial.Serial(strPort, 9600)

        self.ax = deque([0.0] * maxLen)
        self.ay = deque([0.0] * maxLen)
        self.maxLen = maxLen

    # add to buffer
    def addToBuf(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    # add data
    def add(self, data):
        assert (len(data) == 2)
        self.addToBuf(self.ax, data[0])
        self.addToBuf(self.ay, data[1])

    # update plot
    def update(self, frameNum, a0, a1):
        try:
            line = self.ser.readline()
            data = [float(val) for val in line.split()]
            # print data
            if (len(data) == 2):
                self.add(data)
                a0.set_data(range(self.maxLen), self.ax)
                a1.set_data(range(self.maxLen), self.ay)
        except KeyboardInterrupt:
            print('exiting')

        return a0,

        # clean up

    def close(self):
        # close serial
        self.ser.flush()
        self.ser.close()