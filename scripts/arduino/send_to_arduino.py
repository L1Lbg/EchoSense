import serial
import time

# Configura el puerto serial (ajusta el puerto COM según lo que veas en el Administrador de dispositivos de Windows)
arduino = serial.Serial('COM3', 9600)  # Reemplaza 'COM3' por el puerto que corresponde a tu Arduino

def enviar_comando(comando):
    arduino.write(comando.encode())  # Envía el comando al Arduino

# Simulación de un evento (por ejemplo, la detección de algo)
while True:
    evento = str(input("¿Qué fase del semáforo quieres activar? (0: Azul, 1: Rojo, 2: Verde, 3: Amarillo): "))
    enviar_comando(evento)  # El valor se envía directamente, sin restar 1
