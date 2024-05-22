import subprocess

import sys
import glob
import serial

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
