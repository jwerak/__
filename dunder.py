#!/usr/bin/env python2

from gpiozero import  OutputDevice

led6 = OutputDevice(6)
led13 = OutputDevice(13)
led19 = OutputDevice(19)
led26 = OutputDevice(26)

SMALL_SHOT = 1.5
BIG_SHOT = 2.8


led6.off()
led13.off()
led19.off()
led26.off()

time.sleep(2)

led6.on()
led13.on()
led19.on()
led26.on()
