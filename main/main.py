from settings import *
from motor import Motor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motor1 = Motor(20, 21, (14, 15, 18), SPR, CW, RESOLUTION['1/32'])
motor1.step(200, 0.01)
