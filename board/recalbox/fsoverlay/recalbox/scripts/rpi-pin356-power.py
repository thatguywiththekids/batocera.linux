#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def exitAllBatoceraEmulator(channel):
    print 'exitAllBatoceraEmulator'
    os.system('killall retroarch PPSSPPSDL reicast.elf mupen64plus linapple x64')


GPIO.add_event_detect(3, GPIO.FALLING, callback=exitAllBatoceraEmulator,
                      bouncetime=500)

while True:
    time.sleep(0.2)
