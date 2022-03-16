import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   

GPIO.setup(26, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    s = float(input("Скважность: "))
    while(1):
        
        GPIO.output(26, 1)
        time.sleep(0.02/s)
        GPIO.output(26, 0)
        time.sleep(0.02 - 0.02/s)
finally:
    GPIO.output(26, 0)
    GPIO.cleanup()