#!/bin/python

from Character import Character
from Movable import moveRight, moveBack, moveForward, moveLeft

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self._name} : May the gods be with me.")
        self.RPGClass = "Mage"
        self._life = 70
        self._strength = 3
        self._agility = 10
        self._wit = 10

    ''' Overriding methods from Character'''
    def moveRight(self):
        moveRight(self._name, self.RPGClass)

    def moveBack(self):
        moveBack(self._name, self.RPGClass)

    def moveForward(self):
        moveForward(self._name, self.RPGClass)

    def moveLeft(self):
        moveLeft(self._name, self.RPGClass)

    def attack(self, my_weapon):
        if my_weapon == "magic" or my_weapon == "wand":
            print(f"{self._name} : Rrrrrrrrr ....")
            print(f"{self._name} : Feel the power of my {my_weapon} !")

