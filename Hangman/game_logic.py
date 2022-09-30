from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input("Insert a character: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)