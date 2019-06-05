import time
import RPi.GPIO as GPIO

class Motor():

    def __init__(self, dir_pin, step_pin, res_pins, spr, direction, res):
        self.DIR = dir_pin
        self.STEP = step_pin
        self.SPR = spr
        self.currentDir = direction
        self.MODE = res_pins

        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.MODE, GPIO.OUT)

        self.changeDir(direction)
        self.changeResolution(res)
        

    def changeDir(self, direction):
        '''
        0 - Counter clockwise
        1 - Clockwise
        '''
        GPIO.output(self.DIR, direction)
        self.currentDir = direction

    def changeResolution(self, resolution):
        '''
        Change step resolution
        '''
        GPIO.output(self.MODE, resolution)

    def oneStep(self, delay):
        '''
        Take one step in the current direction with given delay
        '''
        GPIO.output(self.STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.STEP, GPIO.LOW)
        time.sleep(delay)

    def step(self, numSteps, delay):
        '''
        Move __ steps with __ delay
        '''
        for i in range(numSteps):
            self.oneStep(delay)
        
