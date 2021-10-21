#!/bin/python
from Mage import Mage
from Warrior import Warrior
from Character import Character

# PARTIE 1 
print("Partie 1")

Eloi = Character("Eloi")
print(Eloi._name)
print(Eloi.RPGClass)
print(Eloi._life)
print(Eloi._agility)
print(Eloi._strength)
print(Eloi._wit)
Eloi.attack("Baton")

