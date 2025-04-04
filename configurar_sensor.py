import RPi.GPIO as GPIO
import time

# Configuración del pin GPIO al que está conectado el sensor PIR
PIR_PIN = 7

# Configurar la biblioteca GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Esperando por el movimiento...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Movimiento detectado!")
            time.sleep(1)  # Espera de 1 segundo para evitar la detección múltiple en un corto período
        else:
            time.sleep(0.1)  # Reduce el uso de CPU cuando no se detecta movimiento
except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")
finally:
    GPIO.cleanup()  # Limpiar la configuración de GPIO al finalizar
