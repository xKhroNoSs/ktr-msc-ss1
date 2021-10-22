#!/bin/python
from Movable import *

class Character:
    def __init__(self, name):
        self._name = name
        self.RPGClass = "Character"
        self._life = 50
        self._agility = 2
        self._strength = 2
        self._wit = 2

    def moveRight(self):
        moveRight(self._name)

    def moveLeft(self):
        moveLeft(self._name)

    def moveBack(self):
        moveBack(self._name)

    def moveForward(self):
        moveForward(self._name)

    def unsheathe(self):
        print(f"{self._name} : unsheathes his weapon.")

    def attack(self, my_weapon):
        print(f"{self._name} : Rrrrrrrrr ....")
