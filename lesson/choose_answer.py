
import os
import random
from Config import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--a", action="store_true", help="Choose english from chinese")
parser.add_argument("-b", "--b", action="store_true", help="Choose chinese from english")
parser.add_argument("-c", "--c", action="store_true", help="Combination")
args = parser.parse_args()
from kanjitool import getShuffledKanjiDataFrame, getTodayWords
today_word_list = getTodayWords(learning_rate)
all_word_list = getShuffledKanjiDataFrame()

# get random row form today_word_list
while True:
    print("---------------------")
    row = today_word_list.sample()
    noise_word = all_word_list.copy()
    #remove row from noise_word
    noise_word = noise_word.drop(row.index)
    mode = 0
    if args.a:
        mode = 0
    elif args.b:
        mode = 1
    elif args.c:
        mode = random.randint(0, 1)
    # switch case for mode
    if mode == 0:
        print(f'which is the english of this word: \n')
        print(row['chinese'].values[0])
        print("Choose the correct english:")
        choices = noise_word.sample(n=number_of_noise_word)['english'].tolist()
        choices.append(row['english'].values[0])
        random.shuffle(choices)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_input = input("Enter the number of the correct english: ")
        while not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            user_input = input("Enter the number of the correct english: ")
        if int(user_input) == choices.index(row['english'].values[0]) + 1:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['english'].values[0]}")
    elif mode == 1:
        print(f'which is the chinese of this word: \n')
        print(f"\"{row['english'].values[0]}\"")
        print("Choose the correct chinese:")
        choices = noise_word.sample(n=number_of_noise_word)['chinese'].tolist()
        choices.append(row['chinese'].values[0])
        random.shuffle(choices)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_input = input("Enter the number of the correct chinese: ")
        while not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            user_input = input("Enter the number of the correct chinese: ")
        if int(user_input) == choices.index(row['chinese'].values[0]) + 1:
            print("\033[92mCorrect!\033[0m")
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {row['chinese'].values[0]}")
    

# Rest of your code goes here