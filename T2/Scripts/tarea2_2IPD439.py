import serial
import struct
import random
import statistics

PORT = '/dev/ttyACM0' 
BAUD = 115200

def send_data():
    data = [random.uniform(-100.0, 100.0) for _ in range(100)]
    formato = '<100f'
    payload = struct.pack(formato, *data)
    head = b'\xAA\xBB\xCC\xDD'
    trama = head + payload
    
    try:
        with serial.Serial(PORT, BAUD, timeout=2) as ser:
            ser.write(trama)
            promedio = sum(data) / len(data)
            var = statistics.pstdev(data) 
            print(f"Teórico -> Media: {promedio:.4f} | Desviación: {var:.4f}")
            
            respuesta = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"STM32   -> {respuesta}")
            
    except serial.SerialException as e:
        print(f"Error abriendo el puerto serial: {e}")

if __name__ == "__main__":
    send_data()
