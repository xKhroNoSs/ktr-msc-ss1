#!/bin/python

def moveRight(name, RPGClass="Character"):
    if RPGClass == "Warrior":
        print(f"{name} : moves right like a bad boy.")

    elif RPGClass == "Mage" :
        print(f"{name} : moves right furtively.")

    elif RPGClass == "Character":
         print(f"{name} : moves right")

def moveLeft(name, RPGClass="Character"):
    if RPGClass == "Warrior":
        print(f"{name} : moves left like a bad boy.")
    elif RPGClass == "Mage":
        print(f"{name} : moves left furtively.")
    elif RPGClass == "Character":
        print(f"{name} moves left.")

def moveForward(name, RPGClass = "Character"):
    if RPGClass == "Warrior":
        print(f"{name} : moves forward like a bad boy.")
    elif RPGClass == "Mage":
        print(f"{name} : moves forward furtively.")

    elif RPGClass == "Character":
        print(f"{name} : moves forward.")

def moveBack(name, RPGClass = "Character"):
    if RPGClass == "Warrior":
        print(f"{name} : moves back like a bad boy.")
    elif RPGClass == "Mage":
        print(f"{name} : moves back furtively.")
    elif RPGClass == "Character":
        print(f"{name} : moves back")
