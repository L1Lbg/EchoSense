import serial

arduino = serial.Serial('COM3', 9600)  # Reemplaza 'COM3' por el puerto que corresponde a tu Arduino

def send_to_arduino(comando):
    arduino.write(comando.encode())  # Envía el comando al Arduino


if __name__ == '__main__':
    while True:
        send_to_arduino(input("(0: Blue, 1: Red, 2: Green, 3: Yellow): "))