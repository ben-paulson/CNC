import time
import RPi.GPIO as GPIO

DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200

MODE = (14, 15, 18)
RESOLUTION = {'Full': (0, 0, 0),
	'Half': (1, 0, 0),
	'1/4': (0, 1, 0),
	'1/8': (1, 1, 0),
	'1/16': (0, 0, 1),
	'1/32': (1, 0, 1)}

GPIO.setmode(GPIO.BCM)
GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE, RESOLUTION['1/32'])
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR * 32
delay = 0.01 / 32

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	time.sleep(delay)

time.sleep(0.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	time.sleep(delay)

GPIO.cleanup()
