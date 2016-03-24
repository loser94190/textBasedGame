
import math
import random

class Enemy:
    kinds = [
        'ogre',
        'goblin',
        'hogoblin',
        'dwarf',
        'bat',
        'snake',
        'dragon',
        'giant ant'
    ]
    attributes = [
        'fat',
        'big',
        'small',
        'strong',
        'normal',
    ]

    #needs work, should depend on the player stats
    def __init__(self, player):
        self.name = self.kinds[math.floor(random.random() * len(self.kinds))]
        self.hp = random.randint(1, 7)
        self.dmg = random.randint(1, 5)
        self.xp = self.dmg*self.hp
        self.surname = self.attributes[random.randint(0,4)]

    #used for attack/hit
    def enemy_take_dmg(self, dmg):
        self.hp -= dmg

    #used to give xp to the player, when the so called player killd the enemy
    def give_xp(self):
        return self.xp

    #returns a string with some information about the enemy
    def explain(self):
        text = 'A %s' %self.surname
        text = text + ' %s' %self.name
        text = text + '(%i dmg, %i hp) '%(self.dmg, self.hp)
        return text