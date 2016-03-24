from .room import Room
from .enemy import Enemy
import os

class Player:
    def __init__(self, name, lvl, game_instance): #constructor

        self.game_instance = game_instance
        self.name = name
        self.location = Room(self.name)

        self.lvl = lvl
        self.max_health = int(lvl*5)
        self.health = self.max_health
        self.dmg_mult = 11
        self.dmg = int(lvl*2*(1+self.dmg_mult))
        self.xp = 0
        self.waited = 0
        self.perks = 0
        self.kill_count = 0
        self.stats = 10
#3 get functions
    def get_dmg(self):
        return self.dmg

    def get_max_hp(self):
        return self.max_health

    def get_xp(self,number):
        self.xp += number

#take_dmg function was only used in testing
    def take_dmg(self, dmg):
        self.health -= dmg
        print("%s, you just lost %i health" % (self.name,dmg))

    def move(self):
        current_room = Room(self.name)
        self.location = current_room

#used when taking inputs
    def act(self, action):
        if action == 'a':
            print('You move weastward.')
            self.move()
            return True
        if action == 's':
            print('You move back.')
            self.move()
            return True
        if action == 'd':
            print('You move eastward.')
            self.move()
            return True
        if action == 'w':
            print('You move forward.')
            self.move()
            return True

        if action == 'explain':
            print(self.explain())
            return True

        if action == 'exit' or action == 'quit':
            print('Are you sure you want to exit? Please type \'yes\'.')
            if input() == 'yes':
                self.game_instance.shutdown()
                return True

        if action == 'wait':
            if self.health < self.max_health:
                self.health += 1
                self.waited += 1
                print('You gained 1 health, your hp now stands at %i' %self.health)
            else:
                print('You already are at full health')
            return True

        if action == 'clear':
            self.clear_scr()
            return True

        action_words = action.split(' ')
        if action_words[0] == 'attack':
            if action_words[1] == '1':
                print('You attack the %s.' % self.location.enemies[0].name)
                self.attack(self.location.enemies[0])
                self.location.check_enemies()

            if action_words[1] == '2':
                print('You attack the %s.' % self.location.enemies[1].name)
                self.attack(self.location.enemies[1])
                self.location.check_enemies()

            if action_words[1] == '3':
                print('You attack the %s.' % self.location.enemies[2].name)
                self.attack(self.location.enemies[2])
                self.location.check_enemies()

            if action_words[1] == '4':
                print('You attack the %s.' % self.location.enemies[3].name)
                self.attack(self.location.enemies[3])
                self.location.check_enemies()

        action_words = action.split(' ')
        if action_words[0] == 'spendperk':
            try:
                self.spend_perks(action_words[2])
            except:
                print("Error spending the perks")
        return True



    def attack(self,enemy):
        while self.health > 0:
            enemy.enemy_take_dmg(self.dmg)
            self.take_dmg(enemy.dmg)
            if enemy.hp <= 0:
                print('You have killed a %s %s' %(enemy.surname, enemy.name))
                self.kill_count += 1
                self.get_xp(enemy.give_xp())
                self.check_lvl_up()
                break
        if self.health <= 0:
            print('The damned %s %s just killed you'%(enemy.surname, enemy.name))
            self.game_instance.shutdown()
        self.location.check_enemies()

    def check_lvl_up(self):
        if self.xp >= self.lvl*10:
            self.lvl += 1
            self.xp = 0
            self.perks += 1
            print('You just leveled up')
        else:
            print('You need %i xp to level up' %(100-self.xp))

    def spend_perks(self, choice):
        if self.perks > 0:
            if choice == 'hp':
                self.health += 5
            elif choice == 'dmg':
                self.dmg += 1
        else:
            print("You don't have any perk poits to spend")

    def clear_scr(self):
        clear = lambda: os.system('cls')
        clear()

    def explain(self):
        clear = lambda: os.system('cls')
        clear()
        text = 'Your name is %s. ' % self.name
        text = text + 'You have %d hit points, out of a maximum of %d. ' % (self.health, self.max_health)
        text = text + '\nYou are level %d, with %d experience points.' % (self.lvl, self.xp)
        text = text + '\nYou currently deal %i damage/hit.' %self.dmg
        if self.waited > 0:
            text = text + '\nYou waited %i times' %self.waited
        if self.kill_count != 1:
            text = text + '\nAnd you killed %i enemies so far ' %self.kill_count
        elif self.kill_count == 1:
            text = text + '\nAnd you killed 1 enemy so far '
        text = text + '\nYou currently have %i perk points to spend.' %self.perks
        text = text + '\nCurrent room:%s' %self.location.description
        return text
