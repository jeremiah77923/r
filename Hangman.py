import os
import random

from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
count = 0
count1 = 0
clue = []
checkCount = 0
isInWord = False
notInWord = False
wrongCount = len(stages)


def convert(string):
    li = list(string)
    return li


def convertlist(list):
    str = ""
    for character in list:
        str += character + " "
    return str


lives = 6
already_guessed = False
final = convert(chosen_word)
for i in range(0, len(chosen_word)):
    clue.append("_")
user_name = input("What is your name?\n")
print(logo)
print(f"Welcome to hangman {user_name}!!!!")
print("Guess a letter each turn, but be careful you only have six lives!")
print("If you get 7 guesses wrong then you will lose ")
while final != clue and True:
    if wrongCount > 1:
        guess = input("Guess a letter\n").lower()
        if len(guess) == 0:
            print("Please enter a guess")
        if guess in clue:
            print(f"You already guessed the letter: {guess}")
        if guess not in chosen_word:
            print(f"You guessed {guess}, and it is not in the word, so you lose a life.")
            wrongCount -= 1
            lives -= 1
    count += 1
    if guess not in clue and len(guess)>0:
        for x in range(len(chosen_word)):
            if chosen_word[x].lower() == guess:
                already_guessed = True
                clue[x] = chosen_word[x]
                checkCount += 1
                isInWord = True
                if checkCount == 1:
                    print(f"You guessed {guess}, and it is in the word. ")
        if isInWord:
            checkCount = 0
        if lives == 0:
            print("You ran out of lives and lost. ")
            print(f"The word was: {chosen_word}")
            break
        print(convertlist(clue))
        print(stages[wrongCount - 1])
        if final == clue:
            print(f"You won and you had {lives} left")
            break
