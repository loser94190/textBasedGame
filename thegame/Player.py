from .room import Room
from .enemy import Enemy

class Player:
    def __init__(self, name, lvl, game_instance):

        self.game_instance = game_instance
        self.name = name
        self.location = Room(self.name)

        self.lvl = lvl
        self.max_health = int(lvl*5)
        self.health = self.max_health
        self.dmg_mult = 11
        self.dmg = int(lvl*2*(1+self.dmg_mult))
        self.xp = 0

    def get_dmg(self):
        return self.dmg

    def get_max_hp(self):
        return self.max_health

    def get_xp(self,number):
        self.xp += number

    def take_dmg(self, dmg):
        self.health -= dmg
        print("%s, you just lost %i health" % (self.name,dmg))

    def move(self):
        current_room = Room(self.name)
        self.location = current_room


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
                print('You gained 1 health, your hp now stands at %i' %self.health)
            else:
                print('You already are at full health')
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


        return True



    def attack(self,enemy):
        while self.health > 0:
            enemy.enemy_take_dmg(self.dmg)
            self.take_dmg(enemy.dmg)
            if enemy.hp <= 0:
                print('You have killed a %s %s' %(enemy.surname, enemy.name))
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
            print('You just leveled up')
        else:
            print('You need %i xp to level up' %(100-self.xp))

    def explain(self):
        text = 'Your name is %s. ' % self.name
        text = text + 'You have %d hit points, out of a maximum of %d. ' % (self.health, self.max_health)
        text = text + 'You are level %d, with %d experience points.' % (self.lvl, self.xp)
        text = text + 'And you currently deal %i damage/hit.' %self.dmg
        text = text + '\n Current room:%s' %self.location.description
        return text
