#!/bin/python

class Character:
    def __init__(self, name):
        self._name = name
        self.RPGClass = "Character"
        self._life = 50
        self._agility = 2
        self._strength = 2
        self._wit = 2

    def attack(self, my_weapon):
        print(f"{self._name} : Rrrrrrrrr ....")
