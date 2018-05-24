#!/usr/bin/env python2

from gpiozero import  OutputDevice

led6 = OutputDevice(6)
led13 = OutputDevice(13)
led19 = OutputDevice(19)
led26 = OutputDevice(26)

SMALL_SHOT = 1.5
BIG_SHOT = 2.8


led6.off()

time.sleep()
