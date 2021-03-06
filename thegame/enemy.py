
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
    def __init__(self, player, player_luck):
        if player > 50 and random.randint(1, 15) == random.randint(1, 10):  #we have a very small chance to get an ennemy DEMON
            self.name = 'DEMON'                             #ge isn't generated at random (only the surname)
            self.surname = self.attributes[random.randint(2,4)]
            self.max_hp = 500
            self.hp = self.max_hp   #doesn't work, for some reason
            self.dmg = 40
            self.xp = 1000
        else:
            self.name = self.kinds[math.floor(random.random() * len(self.kinds))]   #randomly get a name from kinds
            self.max_hp = random.randint(1, random.randint(1,5*player))
            self.hp = self.max_hp
            self.dmg = random.randint(1, random.randint(1,2*player))
            self.xp = self.dmg*self.hp
            if self.hp > player*5:
                self.surname = self.attributes[0]
            elif self.hp > player*5:
                self.surname = self.attributes[1]
            else:
                self.surname = self.attributes[random.randint(2,4)]

    #used for attack/hit
    def enemy_take_dmg(self, dmg, player_luck):
        chance = 3 * player_luck
        if chance >= random.randint(1,100):
            self.hp -= 2*dmg
        else:
            if player_luck > random.randint(5,20):
                true_dmg = math.ceil(dmg * random.randint(7,10) / 10)
            else:
                true_dmg = math.ceil(dmg * random.randint(3,7) / 10)
            if true_dmg >= dmg:
                true_dmg = dmg
            self.hp -= true_dmg
        return true_dmg
    #used to give xp to the player, when the so called player killd the enemy
    def give_xp(self):
        return self.xp

    #returns a string with some information about the enemy
    def explain(self):
        text = 'A %s' %self.surname
        text = text + ' %s' %self.name
        text = text + '(%i dmg, %i hp) '%(self.dmg, self.hp)
        return text

