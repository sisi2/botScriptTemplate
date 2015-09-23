iimport RPi.GPIO as GPIO
import time

def blink(pinA1,pinA2,pinR1,pinR2, n=5):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinA1, GPIO.OUT)
    GPIO.setup(pinA2, GPIO.OUT)
    GPIO.setup(pinR1, GPIO.OUT)
    GPIO.setup(pinR2, GPIO.OUT)
    for i in xrange(n):
        GPIO.output(pinA1, GPIO.HIGH)
        GPIO.output(pinA2, GPIO.HIGH)
        GPIO.output(pinR1, GPIO.LOW)
        GPIO.output(pinR2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pinR1, GPIO.LOW)
        GPIO.output(pinR2, GPIO.LOW)
        GPIO.output(pinA1, GPIO.LOW)
        GPIO.output(pinA2, GPIO.LOW)
        time.sleep(1)
if __name__ == "__main__":
    blink(17,22,18,23)
