from thegame.Game import Game
import os
import pickle
import sys

def logo():
    clear = lambda: os.system('cls')
    clear()
    print('___________                                          ')
    print('\__    ___/__.__.______   ____   ____   ____   ____  ')
    print('  |    | <   |  |\____ \_/ __ \ / ___\_/ __ \ /    \ ')
    print("  |    |  \___  ||  |_> |  ___// /_/  >  ___/|   |  \\")
    print('  |____|  / ____||   __/ \___  >___  / \___  >___|  /')
    print('          \/     |__|        \/_____/      \/     \/ ')

def menu():
    inp = 0
    logo()
    input()
    clear = lambda: os.system('cls')
    clear()
    print('1.New game')
    print('2.Load')
    print('3.Exit')

if __name__ == '__main__':
    menu()
    print('Your choice: ')
    choice = input()
    if choice == '1':
        print('Your name is: ')
        player_name = input()
        G = Game(player_name)
        G.run()
    elif choice == '2':
        gameinFile = open('game_saves.txt', 'rb')
        G = pickle.load(gameinFile)
        gameinFile.close()
        G.run()
    elif choice == '3':
        G = Game('a')
        sys.exit()






