#!/usr/bin/env python

from pprint import pformat


class Item(object):
    """Base class for objects."""

    def __init__(self, description, long_description=None, value=0, damage=0):
        self.description = description
        self.long_description = long_description
        self.value = value
        self.damage = damage

    def __str__(self):
        return pformat(self.__dict__)


class Weapon(Item):
    """Class for weapons that require ammunition."""

    def __init__(self, description, damage, ammo, accuracy, value=0):
        super(Weapon, self).__init__(description, value, damage)
        self.ammo = ammo
        self.accuracy = accuracy


class Armor(Item):
    """Class for items that can be worn for protection."""

    def __init__(self, description, protection, value=0):
        super(Armor, self).__init__(description, value)
        self.protection = protection


class Explosive(Item):
    """Class for items that can be set to blow up."""

    def __init__(self, description, damage, armed, value=0):
        super(Explosive, self).__init__(description, value, damage)
        self.armed = armed


class Consumable(Item):
    """Class for items that can be eaten or drank for health."""

    def __init__(self, description, healing, value=0, damage=0):
        super(Consumable, self).__init__(description, value, damage)
        self.healing = healing


ITEMS = {
    'key': Item(
        description="a small brass key",
        value=1
    ),
    'screwdriver': Item(
        description="a flat-blade screwdriver",
        damage=2
    ),
}

WEAPONS = {
    'handblaster': Weapon(
        description="a sinister looking blaster",
        value=20,
        damage=10,
        ammo=10,
        accuracy=70
    ),
    'laser rifle': Weapon(
        description="a menacing looking laser rifle",
        value=30,
        damage=25,
        ammo=20,
        accuracy=85
    ),
    'proton rifle': Weapon(
        description="a deadly looking proton rifle",
        value=50,
        damage=40,
        ammo=20,
        accuracy=75
    ),
    'grenade': Explosive(
        description="a hand grenade",
        value=10,
        damage=50,
        armed=False
    ),
}

ARMOR = {
    'leather gloves': Armor(
        description="a worn pair of leather gloves",
        value=5,
        protection=5
    ),
}

CONSUMABLES = {
    'wet noodle': Consumable(
        description="a strand of limp spaghetti",
        damage=1,
        healing=1
    ),
}
