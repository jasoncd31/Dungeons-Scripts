# Created by Jason Douglas
# @jasoncd31 on GitHub

import random

title = '''
    |----------------|
    |   Dice Roller  |
    |       V.1      |
    |----------------|
    '''

commands = '''
    r s/t diceTotal diceSides - Roll (separate/total) diceTotal diceSides
    a - add
    h - help
    e or q - Exit
'''

def diceRoll(sides):
    return random.randint(1,sides)

def multipleDiceTotal(number, sides):
    total = 0
    for i in range(number):
        total += diceRoll(sides)
    return total

def multipleDiceSeparate(number, sides):
    rolls = []
    for i in range(number):
        rolls.append(diceRoll(sides))
    return rolls

def main():
    print(title)
    print("~~~~~~~~~~~~~~~~")
    while(True):
        print(commands)
        print("Enter A Command")
        print("----------------")
        command = input()
        print("----------------")
        command_split = command.split(" ")
        match command_split[0]:
            case "h":
                print(commands)
            case "e" | "exit" | "q" | "quit":
                break
            case "r":
                if len(command_split) != 4:
                    print("Invalid Command")
                match command_split[1]:
                    case "s":
                        print(multipleDiceSeparate(int(command_split[2]), int(command_split[3])))
                    case "t":
                        print(multipleDiceTotal(int(command_split[2]), int(command_split[3])))
                    case _:
                        print("Invalid Command")
            case "a" | "add":
                if len(command_split) == 3:
                    print(int(command_split[1]) + int(command_split[2]))
                else:
                    print("Invalid Command")
            case _:
                print("Invalid Command")
        print("----------------")

main()