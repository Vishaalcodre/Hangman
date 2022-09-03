# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:55:01 2022

"""
import random
import hangman_words
from hangman_art import logo,stages

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])

print(f"The chosen word is {chosen_word}")
