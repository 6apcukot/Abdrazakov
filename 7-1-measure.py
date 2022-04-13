import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
cad = [10, 9, 11, 5, 6, 13, 19, 26]
mas = [0, 0, 0, 0, 0, 0, 0, 0]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
led = []
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

i = 0
def adc():
    
    for i in 7, 6, 5, 4, 3, 2, 1, 0:
        #print(i)
        GPIO.output(cad[i], 1)
        mas[7 - i] = 1
        time.sleep(0.007)
        if(GPIO.input(comp) == 0):
            GPIO.output(cad[i], 0)
            mas[7-i] = 0
            
#def adc():
#    for i in range(256):
#        GPIO.output(dac, decimal2binary(i))
#        time.sleep(0.001)
#        if(GPIO.input(comp) == 0):
 #           break
 #   return i        

try:
    while(1):
        
        #v = adc()
        v = 0
        mas = [0, 0, 0, 0, 0, 0, 0, 0]
        GPIO.output(dac, mas)
        adc()
        for j in range(8):
            v += mas[j]*(2**(7-j))
        volt = v*3.3/256
        print(v, "  ", volt)
        GPIO.output(leds, 0)
        k = 0
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                    #print(j)
                break    
        

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()