from .room import Room

import os
import pickle

##########################################
#Problems:                               #
#   When you level up, the xp is always 0#
#   Some attack errors                   #
#                                        #
##########################################

class Player:
    def __init__(self, name, lvl, game_instance): #constructor

        self.game_instance = game_instance
        self.name = name
        self.location = Room(self)                 #set the current location as a Room

        self.lvl = lvl                              #it's not default 1 for testing purposes
        self.max_health = int(lvl*5)                #it's an int, for some reason
        self.health = self.max_health               #health changes value, max_health always stays the same
        self.dmg_mult = 0.5                         #some weird thing i thought of
        self.dmg = lvl*2*(1+self.dmg_mult)
        self.xp = 0                                 #xp starts from 0
        self.waited = 0
        self.perks = 0
        self.kill_count = 0

#3 get functions
    def get_dmg(self):
        return self.dmg_mult

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
        if action == 'save':
            self.save()
            return True

        if action == 'load':
            self.load()
            return True

        if action == 'help':
            self.help()
            return True

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
            try:                            #for some reason, sometimes we get an error
                if action_words[1] == '1':  #but it doesn't do anything
                    print('You attack the %s.' % self.location.enemies[0].name)
                    self.attack(self.location.enemies[0])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '2':
                    print('You attack the %s.' % self.location.enemies[1].name)
                    self.attack(self.location.enemies[1])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '3':
                    print('You attack the %s.' % self.location.enemies[2].name)
                    self.attack(self.location.enemies[2])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '4':
                    print('You attack the %s.' % self.location.enemies[3].name)
                    self.attack(self.location.enemies[3])
                    self.location.check_enemies()
                    return True
            except:
                print("Error")

        action_words = action.split(' ')
        if action_words[0] == 'hit':
            try:
                if action_words[1] == '1':
                    print('You attack the %s.' % self.location.enemies[0].name)
                    self.hit(self.location.enemies[0])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '2':
                    print('You attack the %s.' % self.location.enemies[1].name)
                    self.hit(self.location.enemies[1])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '3':
                    print('You attack the %s.' % self.location.enemies[2].name)
                    self.hit(self.location.enemies[2])
                    self.location.check_enemies()
                    return True

                if action_words[1] == '4':
                    print('You attack the %s.' % self.location.enemies[3].name)
                    self.hit(self.location.enemies[3])
                    self.location.check_enemies()
                    return True
            except:
                print("Error")

        action_words = action.split(' ')
        if action_words[0] == 'spendperk':  #here we split the spendperk #something
            try:
                self.spend_perks(action_words[1])
                return True
            except:
                print("Error spending the perks")
                return False


    #   this is used to attack an enemy and keep on doing that
    #   until either the player or the enemy is dead
    def attack(self,enemy):
        while self.health > 0:
            enemy.enemy_take_dmg(self.dmg)      #when your health is greater than 0, you deal dmg to an enemy
            if enemy.hp > 0:
                self.take_dmg(enemy.dmg)        #you only take dmg if the hp of the enemy is greater than 0
            if enemy.hp <= 0:
                if enemy.name == 'DEMON':
                    print('Congrats, you just killed a DEMON, you gain 3 dmg')
                    self.dmg += 3
                else:
                    print('You have killed a %s %s' %(enemy.surname, enemy.name))
                self.kill_count += 1            #counts the enemies killed
                self.get_xp(enemy.give_xp())    #you gain xp by killing an enemy
                self.check_lvl_up()             #check if the player has enough xp to lvl up
                break
        if self.health <= 0:
            print('The damned %s %s just killed you'%(enemy.surname, enemy.name))
            self.game_instance.shutdown()
        self.location.check_enemies()

    #used to check if the player need to level up
    #it's called after gaining xp (killing enemies)
    def check_lvl_up(self):
        if self.xp >= self.lvl*10:
            self.lvl += 1
            self.xp = 0     #this is a bit wrong
            self.perks += 1
            print('You just leveled up')
        else:
            print('You need %i xp to level up' %(self.lvl*10-self.xp))

    #spends a perk and the player gains health/dmg/dmg_mult
    def spend_perks(self, choice):
        if self.perks > 0:
            if choice == 'hp':
                self.max_health += 5
                self.health += 5
                print('\n\nYou gained 5 health points(total)')
                self.perks -= 1
            elif choice == 'dmg':
                self.dmg += 3
                print('\n\nYou gained 3 dmg')
                self.perks -= 1
            elif choice == 'dmg_mult':
                self.dmg_mult += 0.5
                self.dmg = self.lvl*(1+self.dmg_mult)
                print('\n\nYou gained 1 dmg multiplier')
                self.perks -= 1
            else:
                return False
        else:
            print("You don't have any perk poits to spend")

    #clear screen (console) function
    def clear_scr(self):
        clear = lambda: os.system('cls')
        clear()

    #prints commands used by the player
    def help(self):
        print('\nHere are some of the commands you will use:')
        print('-> explain         : you get general information about yourself and your surroundings')
        print('-> move            : you can move using a,s,w,d')
        print('-> attack #        : you can attack an enemy indicating it\'s possition')
        print('-> hit #           : similar to attack, but only hits one time')
        print('-> spendperk #perk : you can spend a perk, gaining hp or dmg(hp, dmg, dmg_mult)')
        print('-> clear           : clears the screen(console)')
        print('-> wait            : you wait a bit, gaining 1 hp')
        print('-> exit/quit       : you can quit the game')
        print('-> help            : i guess you already know what it does\n')

    #similar to attack, but attack only once, not until someone dies
    #it hits the target for the player's dmg
    #the player gets hit for the target's dmg
    def hit(self,enemy):
        enemy.enemy_take_dmg(self.dmg)      #when your health is greater than 0, you deal dmg to an enemy
        if enemy.hp > 0:
            self.take_dmg(enemy.dmg)        #you only take dmg if the hp of the enemy is greater than 0
        if enemy.hp <= 0:
            print('You have killed a %s %s' %(enemy.surname, enemy.name))
            self.kill_count += 1            #counts the enemies killed
            self.get_xp(enemy.give_xp())    #you gain xp by killing an enemy
            self.check_lvl_up()             #check if the player has enough xp to lvl up
        if self.health <= 0:
            print('The damned %s %s just killed you with just one hit'%(enemy.surname, enemy.name))
            self.game_instance.shutdown()
        self.location.check_enemies()

    #Clear the screen and then returns a string with several
    #things about the player and his current Room
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
        text = text + '\n%s' %self.location.description
        return text

    def save(self):
        outFile = open('saves.txt', 'wb')
        pickle.dump(self,outFile)
        outFile.close()

    def load(self):
        inFile = open('saves.txt', 'rb')
        self = pickle.load(inFile)
        inFile.close()