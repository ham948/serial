# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:29:06 2019

@author: Daniel
"""

import time
import serial

lns = serial.Serial(
        port='/dev/serial0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

while 1:
    lns.write('hello!\n')
    time.sleep(1)