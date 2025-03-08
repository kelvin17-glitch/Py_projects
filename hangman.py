import random
import time
from collections import Counter

# Make text gen game-like
def slow_print(text, delay=0.09):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# The secret list ;) ..."All fruits known to man"
fruits = ["Apple", "Banana", "Orange", "Grape", "Mango", "Pineapple", "Watermelon", "Papaya", "Pear", "Plum", "Peach", "Strawberry", "Raspberry", "Blackberry", 
    "Blueberry", "Cherry", "Avocado", "Dragon Fruit", "Passion Fruit", "Lychee", "Rambutan", "Durian", "Mangosteen", "Starfruit", "Jackfruit", "Longan", "Soursop", "Salak", "Feijoa", 
    "Custard Apple", "Miracle Fruit", "Lemon", "Lime", "Tangerine", "Clementine", "Pomelo", "Yuzu", "Bergamot", 
    "Finger Lime", "Kumquat", "Cranberry", "Goji Berry", "Elderberry", "Boysenberry", "Loganberry", "Mulberry", "Cloudberry", "Gooseberry", "Apricot", "Nectarine", "Chokecherry", "Jujube", "Cantaloupe", "Honeydew", "Casaba Melon", "Galia Melon", "Korean Melon", "Breadfruit", "Plantain", "Ackee", "Coconut", "Chestnut", "Hazelnut", "Persimmon", "Medlar", "Loquat", "Jabuticaba", "Noni", "Buffaloberry", "Nutmeg", "Allspice", "Clove", "Elderberry", "Juniper Berry", "Grapes", "Sloe"]

# Pick a fruit
word = random.choice(fruits).lower()

# Intro text
print("Hey! Let's play a game!")
print()
print("I'm gonna think of a word. You're going to guess what it is.")
print("Ready? Let's Go!")

# The clue
print("Here's the word's 'skeleton': ")
for char in word:
    print("__", end=" ")
print()

# String of guessed letters
guessStr = ''

# Limit max number of chances to guess
chances = len(word) + 2
flag = 0

# Game logic
print()
slow_print(f"First guess of {chances}! Hope you lucky...")
slow_print("Big hint! The word's a fruit:)")
print(word)
print()

while (chances != 0) and (Counter(guessStr) != Counter(word)):
    chances -= 1
    # Get input
    guess = str(input("Enter a letter: "))

    # Check no of occurrences of guess in word
    c = word.count(guess)
    for l in range(c):
        guessStr += guess

    # Show user current status
    for char in word:
        if char in guessStr:
            print(char, end=' ')
        else:
            print("__", end=' ')
    print()

    # If guess is correct
    if Counter(guessStr) == Counter(word):
        slow_print(f"Congrats! You guessed right with {chances} chances remaining!")
        slow_print(f"The word was {word}.")
        break

print()
slow_print(f"You lose! The word was {word}!")
slow_print("Better luck next time!")
    

