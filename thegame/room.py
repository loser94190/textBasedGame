from .enemy import Enemy

import math
import random


class Room:
    flavour_a = [
        'The room is large.',
        'The room is medium-sized.',
        'The room is small.',
        'The room is cramped.' ]

    flavour_b = [
        'The walls are covered is moss.',
        'There\'s a candle in the center of the room.',
        'The walls are wet.',
        'There\'s a crack in the rock wall.' ]

    flavour_c = [
        'You have an uneasy feeling regarding this room.',
        'You can feel a draught.',
        'You step into a puddle.',
        'It\'s quite cold.' ]

    def __init__(self, playername):

        #   room generation
        random_flavour_a = self.flavour_a[math.floor(random.random() * len(self.flavour_a))]
        random_flavour_b = self.flavour_b[math.floor(random.random() * len(self.flavour_b))]
        random_flavour_c = self.flavour_c[math.floor(random.random() * len(self.flavour_c))]

        #   Enemy generation
        self.enemy_count = math.floor(random.random() * 4) + 1
        self.enemies = [Enemy(playername) for i in range(0, self.enemy_count)]
        for i in range(0, self.enemy_count):
            if "DEMON" in self.enemies[i].name:
                self.enemy_count = 1

        self.description = random_flavour_a + ' ' + random_flavour_b + ' ' + random_flavour_c + '\n'
        self.room_desc = self.description

        #   room description
        self.description += 'There are %d enemies here: ' % self.enemy_count
        for i in range(0, self.enemy_count):
            self.check_enemies()
            self.description += self.enemies[i].explain()
            if i < self.enemy_count-1:
                self.description += ', '
        self.description += '.'

    #removes an enemy if he dies
    def check_enemies(self):
        for i in self.enemies:
            if i.hp <= 0:
                self.enemies.remove(i)
                self.description = self.room_desc
                self.enemy_count -= 1
                self.description += 'There are %d enemies here: ' % self.enemy_count
                for i in range(0, self.enemy_count):
                    self.check_enemies()
                    self.description += self.enemies[i].explain()
                    if i < self.enemy_count-1:
                        self.description += ', '
                self.description += '.'



    def explain(self):
        return self.description

