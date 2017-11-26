import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 21

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

def trigger():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

def readEcho():
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    return pulse_duration

def ping():
    trigger()
    return round(readEcho() * 17150, 2)
