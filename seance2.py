import RPi.GPIO as GPIO
import time

def blink(pinA1,pinA2,pinR1,pinR2,  n=5):
    GPIO.setmode(GPIO.BCM)
    GPIO.setUP(pinA1,  GPIO.OUT)
    GPIO.setUP(pinA2,  GPIO.OUT)
    GPIO.setUP(pinR1,  GPIO.OUT)
    GPIO.setUP(pinR2,  GPIO.OUT)
    for i in xrange(n):
        GPIO.output(pinA1,  GPIO.HIGHT)
        GPIO.output(pinA2,  GPIO.HIGHT)
        GPIO.output(pinR1,  GPIO.LOW)
        GPIO.output(pinR2,  GPIO.LOW)
        time.sleep(1)
        GPIO.output(pinR1,  GPIO.LOW)
        GPIO.output(pinR2,  GPIO.LOW)
        GPIO.output(pinA1,  GPIO.LOW)
        GPIO.output(pinA2,  GPIO.LOW)
        time.sleep(1)
if __name__ == "__main__":
    blink(17,22,18,23)
