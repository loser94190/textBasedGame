from .Player import Player
import pickle

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name,1, self)
        self.running = True

    def run(self):
        print('Welcome, %s!' % self.player.name)
        self.player.help()

        while self.running:
            ret = self.take_input()

            if ret == 'Save':
                self.save()
            if not ret:
                print('I didn\'t understand that.')

    def take_input(self):
        return self.player.act(input())

    def shutdown(self):
        self.running = False

    def save(self):
        outFile = open('game_saves.txt', 'wb')
        pickle.dump(self,outFile)
        outFile.close()