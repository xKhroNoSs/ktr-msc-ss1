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

Ryan = Warrior("Ryan")
Hugo = Mage("Hugo")

Ryan.attack("sword")
Hugo.attack("wand")

# PARTIE 3
print("Partie 3")

Henri = Warrior("Henri")
Dominique = Mage("Dominique")

Henri.moveRight()
Henri.moveLeft()
Henri.moveBack()
Henri.moveForward()

Dominique.moveRight()
Dominique.moveLeft()
Dominique.moveBack()
Dominique.moveForward()

# PARTIE 4
print("Partie 4")
Luc = Character("Luc")
Jean = Warrior("Jean")
Billy = Mage("Billy")

Luc.moveRight()
Luc.moveLeft()
Luc.moveBack()
Luc.moveForward()

Jean.moveRight()
Jean.moveLeft()
Jean.moveBack()
Jean.moveForward()

Billy.moveRight()
Billy.moveBack()
Billy.moveLeft()
Billy.moveForward()
