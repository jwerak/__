#!/usr/bin/env python2

from gpiozero import OutputDevice
import time

led6 = OutputDevice(6)
led13 = OutputDevice(13)
led19 = OutputDevice(19)
led26 = OutputDevice(26)

SMALL_SHOT = 1.5
BIG_SHOT = 2.8

receipts = {
    'cubalibre': {'rum': 3, 'cola': 25},
    'git&tonic': {'gin': 3, 'tonic': 25}
}


def turn_off():
    led6.off()
    led13.off()
    led19.off()
    led26.off()


def turn_on():
    led6.on()
    led13.on()
    led19.on()
    led26.on()


def serve_drink(name):
    print("Serving drink: {0}".format(name))
    for ingredience in receipts[name]:
        print ingredience


serve_drink('cubalibre')
