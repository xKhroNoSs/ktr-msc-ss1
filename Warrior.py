#!/bin/python

from Character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self._name} : My name will go down in the history!")
        self.RPGClass = "Warrior"
        self._life = 100
        self._strength = 10
        self._agility = 8
        self._wit = 3

    def attack(self, my_weapon):
        if my_weapon == "hammer" or my_weapon == "sword":
            print(f"{self._name} : Rrrrrrrrr ....")
            print(f"{self._name} : I ' ll crush you with my {my_weapon} !")

