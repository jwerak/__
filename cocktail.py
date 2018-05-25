#!/usr/bin/env python2

from gpiozero import OutputDevice
import time


class Ingredient(OutputDevice):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super(Ingredient, self).__init__(*args, **kwargs)

    def infuse(self, seconds):
        print(
            'Infusing {} ({}) for {} seconds'.format(
                self.name, self.pin, seconds))
        self.off()
        time.sleep(seconds)
        self.on()
        print('Infusion of {} completed'.format(self.name))


_ingredients = [
    Ingredient('rum', pin=6),
    Ingredient('cola', pin=13),
    Ingredient('gin', pin=19),
    Ingredient('tonic', pin=26)]


_receipts = {
    'cubalibre': [('rum', 3), ('cola', 25)],
    'gintonic': [('gin', 3), ('tonic', 25)]}


def _all_off():
    for i in _ingredients:
        i.on()


def _all_on():
    for i in _ingredients:
        i.off()


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
        for i in [item for item in _ingredients if item.name == ingredient]:
            print('Found {} on {}'.format(i.name, i.pin))
            i.infuse(duration)


print('Ready to prepare these drinks:')
print drinks()
print('from these ingredients:')
print ingredients()
_all_off()
