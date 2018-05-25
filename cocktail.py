#!/usr/bin/env python2

from gpiozero import OutputDevice
import time


class Ingredient(OutputDevice):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super(Ingredient, self).__init__(*args, **kwargs)

    def infuse(self, seconds):
        print('Infusing {} ({}) for {} seconds', self.name, self.pin, seconds)
        self.on()
        time.sleep(seconds)
        self.off()
        print('Infusion of {} completed', self.name)


_ingredients = [
    Ingredient('rum', pin=6, active_high=False),
    Ingredient('cola', pin=13, active_high=False),
    Ingredient('gin', pin=19, active_high=False),
    Ingredient('tonic', pin=26, active_high=False)]


_receipts = {
    'cubalibre': [('rum', 3), ('cola', 25)],
    'gintonic': [('gin', 3), ('tonic', 25)]}


def _all_off():
    for i in _ingredients:
        i.off()


def _all_on():
    for i in _ingredients:
        i.on()


def drinks():
    return _receipts


def ingredients():
    return [i.name for i in _ingredients]


def serve_drink(name):
    if name not in _receipts.keys():
        print('Unknown drink {}'.format(name))
        return
    print('Serving drink: {0}'.format(name))
    for ingredient, duration in _receipts[name]:
        print('Ingredient {} duration {}'.format(ingredient, duration))
        for i in [i for i in _ingredients if i.name == name]:
            i.infuse(duration)


print('Ready to prepare these drinks:')
print drinks()
print('from these ingredients:')
print ingredients()
_all_off()
