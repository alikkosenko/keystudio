import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 18  # или другой пин
GPIO.setup(pin, GPIO.IN)

while True:
    print(GPIO.input(pin))
    time.sleep(0.5)

