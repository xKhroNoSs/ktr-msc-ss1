#!/bin/python
from Mage import Mage
from Warrior import Warrior
from Character import Character

# PARTIE 1 
print("Partie 1")

character = Character("Eloi")
print(character._name)
print(character.RPGClass)
print(character._life)
print(character._agility)
print(character._strength)
print(character._wit)
character.attack("Baton")

# PARTIE 2
print("Partie 2")

warrior = Warrior("Ryan")
mage = Mage("Hugo")

warrior.attack("sword")
mage.attack("wand")
