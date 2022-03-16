import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   
pin = 22

GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)




try:
    while(1):
        s = float(input("Скважность: "))
        if s == 0:
            s = 1
        p.start(1/s*100)
        
        if input("Press q to stop: ") == 'q':
            p.stop()
            break
finally:
    GPIO.output(pin, 0)
    GPIO.cleanup()