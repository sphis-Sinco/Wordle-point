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

def gameplay():
        import time, random

        current_round = 0
        current_word = ""
        current_guess = 1
        
        while current_round < PLAY_ROUNDS:
                current_round = current_round + 1
                current_word = AVAILIBLE_WORDS[random.randint(0, AVAILIBLE_WORDS.__len__())]
                current_guess = 1

                wins = 0
                loses = 0

                print(f'Round {current_round}: Word is {current_word.__len__()} letters long, {PLAY_GUESSES} guesses.')

                while not current_guess == PLAY_GUESSES:
                        player_input = input('> ')

                        if player_input == 'seasheels':
                                player_input = current_word
                                print('word is '+current_word)
                        else:
                                if player_input.__len__() > current_word.__len__():
                                        print('Your guess was too long.')

                        corrects = []
                        almosts = []
                        incorrects = []

                        int = 0

                        for i in player_input:
                                if player_input.__len__() > current_word.__len__():
                                        incorrects.append(i)
                                        continue

                                if current_word.__contains__(i):
                                        if current_word[int] == i:
                                                print(f'{i} is in the right position')
                                                corrects.append(i)
                                        else:
                                                print(f'{i} is not in the right position')
                                                almosts.append(i)
                                else:
                                        print(f'{i} is not in the word')
                                        incorrects.append(i)

                                int = int + 1
                        

                        if player_input == current_word:
                                current_guess = PLAY_GUESSES
                                wins = wins + 1
                        else:
                                print(f'Corrects: {corrects.__len__()}\nAlmosts: {almosts.__len__()}\nIncorrects: {incorrects.__len__()}')
                                print(f'{PLAY_GUESSES - current_guess} guesses left')
                                current_guess = current_guess + 1
                        
                        if current_guess == PLAY_GUESSES:
                                loses = loses + 1
        
        print(f'You won {wins} rounds and lost {loses} rounds!')
        time.sleep(10)
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
                        MENU = gameplay()
                case 2:
                        CANT_SET = True
                        MENU = 0

else:
        print('Bye bye!')