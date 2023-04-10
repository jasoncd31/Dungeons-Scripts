# Created by Jason Douglas
# @jasoncd31 on GitHub

import random

charStats = {"STR" : 0, "DEX" : 0, "CON" : 0, "INT" : 0, "WIS" : 0, "CHA" : 0}

def rollStat():
    rolls = []
    for i in range(4):
        rolls.append(diceRoll(6))
    rolls.sort()
    rolls.pop(0)
    return sum(rolls)

def diceRoll(sides):
    return random.randint(1,sides)

def rollAll():
    for stat in charStats:
        charStats[stat] = rollStat()

def printStats():
    for stat in charStats:
        print(stat, charStats[stat])

print(diceRoll(20))
