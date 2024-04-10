import serial
import binascii

com = "/dev/cu.usbserial-0001"

con = serial.Serial(com, baudrate=115200, timeout=5)
while True:
    header = con.read(size=2)
    print(binascii.hexlify(header))

    msg_type = con.read(size=1)
    print(binascii.hexlify(msg_type))

    package_id = con.read(size=1)
    print(binascii.hexlify(package_id))

    message_size = con.read(size=2)
    print(binascii.hexlify(message_size))

    body = con.read(size=int.from_bytes(message_size, byteorder="big"))
    print(binascii.hexlify(body))

    if msg_type == bytes.fromhex("20"):
        print("received debug message:")
        print(body)

con.close()