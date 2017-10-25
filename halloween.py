#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
	if (GPIO.input(22) == False):
        os.system('echo "connect AA:BB:CC:DD:EE:FF\nquit" | bluetoothctl &')

    if (GPIO.input(23) == False):
        os.system('mpg123 -q file1.mp3 &')

    if (GPIO.input(24) == False):
        os.system('mpg123 -q file2.mp3 &')

    if (GPIO.input(25)== False):
        os.system('mpg123 -q file3.mp3 &')

    sleep(0.1);