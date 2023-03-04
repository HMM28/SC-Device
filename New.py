import RPi.GPIO as GPIO
import time
import os
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(2 ,GPIO.IN)
prev_input = 1

while True:
        input = GPIO.input(2)

        if ((not prev_input) and input):
            os.system("python /home/group4/Desktop/t5.py")

        prev_input = input

        time.sleep(.05)

