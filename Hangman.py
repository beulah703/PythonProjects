import random
from words import words
from hangman_visual import lives_visual_dict
import string


@@ -29,7 +30,7 @@ def hangman():
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6
    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
@@ -39,6 +40,7 @@ def hangman():

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
@@ -60,6 +62,7 @@ def hangman():

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
