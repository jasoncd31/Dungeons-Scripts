# Created by Jason Douglas
# @jasoncd31 on GitHub

from genericCharacter import genericCharacter

group = []

title = '''
--------------------------------
|                              |
|       Health Tracker         |
|            V.1               |
|                              |
--------------------------------
'''

commands = '''
1. Add Character
2. Print Group
3. Damage Character
4. Heal Character
5. Exit
'''

def addCharacter(name, health):
    group.append(genericCharacter(name, health))

def printGroup():
    for character in group:
        print(character.getName(), character.getHealth())

def main():
    print(title)
    while(True):
        print(commands)
        print("Current Group:")
        printGroup()
        print()
        command = input()
        if command == "1":
            print("Enter Name")
            name = input()
            print("Enter Health")
            health = int(input())
            addCharacter(name, health)
            print("Added", name, "with", health, "health")
        elif command == "2":
            print()
            print("--Group--")
            printGroup()
        elif command == "3":
            print("Enter Name")
            name = input()
            print("Enter Damage")
            damage = int(input())
            for character in group:
                if character.getName() == name:
                    character.damage(damage)
        elif command == "4":
            print("Enter Name")
            name = input()
            print("Enter Heal")
            heal = int(input())
            for character in group:
                if character.getName() == name:
                    character.heal(heal)
        elif command == "5":
            break
        print("----------------")


main()