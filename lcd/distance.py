from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=21, trigger=16)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
