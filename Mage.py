#!/bin/python

from Character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self._name} : May the gods be with me.")
        self.RPGClass = "Mage"
        self._life = 70
        self._strength = 3
        self._agility = 10
        self._wit = 10

    def attack(self, my_weapon):
        if my_weapon == "magic" or my_weapon == "wand":
            print(f"{self._name} : Rrrrrrrrr ....")
            print(f"{self._name} : Feel the power of my {my_weapon} !")

