from word_manager import *
from game_info import *
from game_play_info import *

AVAILIBLE_WORDS = getWords()

# Menu Integers
# 0 - title
# 1 - play
# 2 - settings
# -1 - game over
MENU = 0

SETTINGS = {}

print(f'{GAME_NAME} Iteration {GAME_ITERATION}')

def title_menu():
        player_input = int(input('What would you like to do?\n\n1 - Play\n2 - Settings\n3 - Leave\n\n> '))
        match player_input:
                case 1:
                        return 1
                case 2:
                        return 2
                case 3:
                        return -1
        
        return 0

CANT_SET = False

while not MENU == -1:
        import subprocess
        import os
        
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

        if CANT_SET:
                print('You cant do settin')
                CANT_SET = False

        match MENU:
                case 0:
                        MENU = title_menu()
                case 1:
                        print('PLAY')
                case 2:
                        CANT_SET = True
                        MENU = 0

else:
        print('Bye bye!')