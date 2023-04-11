# Created by Jason Douglas
# @jasoncd31 on GitHub


class genericCharacter:
    def __init__(self, name, health):
        self.name = name
        self.maxHealth = health
        self.currentHealth = health
    
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.currentHealth
    
    def getMaxHealth(self):
        return self.maxHealth
    
    def damage(self, amount):
        self.currentHealth -= amount
        if self.currentHealth <= 0:
            self.currentHealth = 0
            self.die()  # This is a function that can be overridden by subclasses

    def heal(self, amount):
        self.currentHealth += amount
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth

