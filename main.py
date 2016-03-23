from thegame.Game import Game

if __name__ == '__main__':
    print('Your name: ')
    player_name = input()
    G = Game(player_name)

    G.run()
