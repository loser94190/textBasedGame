
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
        if random.randint(1,150) == random.randint(1,100):  #we have a very small chance to get an ennemy DEMON
            self.name = 'DEMON'                             #ge isn't generated at random (only the surname)
            self.surname = self.attributes[random.randint(2,4)]
            self.max_hp = 500
            self.hp = self.max_hp   #doesn't work, for some reason
            self.dmg = 40
            self.xp = 1000
        else:
            self.name = self.kinds[math.floor(random.random() * len(self.kinds))]   #randomly get a name from kinds
            self.max_hp = random.randint(1, random.randint(1,55))                   #get a random hp between 1 and
            self.hp = self.max_hp                                                   #a random nr
            self.dmg = random.randint(1, random.randint(1,35))                      #just like the hp
            self.xp = self.dmg*self.hp
            if self.hp > 5:                                                         #to add some flavor
                self.surname = self.attributes[0]
            elif self.hp > 15:
                self.surname = self.attributes[1]
            else:
                self.surname = self.attributes[random.randint(2,4)]

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