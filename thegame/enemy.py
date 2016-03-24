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


    def __init__(self, player_stats):
        self.name = self.kinds[math.floor(random.random() * len(self.kinds))]
        self.hp = random.randint(1, 11)
        self.dmg = random.randint(1, 5)
        self.xp = self.dmg*self.hp / 3
        self.surname = self.attributes[random.randint(0,4)]

    def enemy_take_dmg(self, dmg):
        self.hp -= dmg

    def give_xp(self):
        return self.xp

    def explain(self):
        text = 'A %s' %self.surname
        text = text + ' %s' %self.name
        text = text + '(%i dmg, %i hp) '%(self.dmg, self.hp)
        return text