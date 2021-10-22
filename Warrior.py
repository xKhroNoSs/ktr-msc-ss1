#!/bin/python

from Character import Character
from Movable import moveRight, moveBack, moveForward, moveLeft

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self._name} : My name will go down in the history!")
        self.RPGClass = "Warrior"
        self._life = 100
        self._strength = 10
        self._agility = 8
        self._wit = 3

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
        if my_weapon == "hammer" or my_weapon == "sword":
            print(f"{self._name} : Rrrrrrrrr ....")
            print(f"{self._name} : I ' ll crush you with my {my_weapon} !")

