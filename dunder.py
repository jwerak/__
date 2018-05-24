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
    'cubalibre': [('rum', 3), ('cola', 25)],
    'gintonic': [('gin', 3), ('tonic', 25)]
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


def pump_ingredients(name, duration):
    if name == 'rum':
        print "Rum for {} seconds".format(duration)
        led6.on()
        time.sleep(duration)
        led6.off()
    if name == 'cola':
        print "Cola for {} seconds".format(duration)
        led13.on()
        time.sleep(duration)
        led13.off()
    if name == 'gin':
        print "Gin for {} seconds".format(duration)
        led19.on()
        time.sleep(duration)
        led19.off()
    if name == 'tonic':
        print "Tonic for {} seconds".format(duration)
        led26.on()
        time.sleep(duration)
        led26.off()


def drinks():
    return receipts


def ingredients():
    ing = []
    for r in receipts:
        for i in r:
            ing.append(i[0])
    return ing


def serve_drink(name):
    print("Serving drink: {0}".format(name))
    for ingredients in receipts[name]:
        pump_ingredients(ingredients[0], ingredients[1])


print drinks()
print ingredients()
turn_off()
serve_drink('cubalibre')
serve_drink("gintonic")
