import serial

ser = serial.Serial('/dev/ttyACM0', 115200, parity=serial.PARITY_EVEN, timeout=1)
ser.write(b'\x7F')
print("", ser.read(1).hex())
ser.write(b'\x11\xEE')
print("", ser.read(1).hex())
ser.write(b'\x08\x00\x00\x00\x08')
print("", ser.read(1).hex())
ser.write(b'\xFF\x00')
print("", ser.read(1).hex())
datos = ser.read(256)
print(datos.hex(' '))
ser.close()
