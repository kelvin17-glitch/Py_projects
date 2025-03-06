import random
import time

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
comp_pick = random.choice(fruits).lower()
print(comp_pick)
# Limit max number of chances to guess
max_chances = len(comp_pick) + 2
chances = 0

# Get first guess
guess = input("Gimme gimme gimme!: ")
letter_list = list(comp_pick)

# Append a reference list on first guess
result = []
for v in letter_list:
    if v == guess:
        result.append(v)
    else:
        result.append("-")
chances += 1

# The Game logic
comp = ''.join(letter_list)
print(result)
while chances < max_chances:
    guess = input("Gimme gimme gimme!: ")
    for i, v in enumerate(letter_list):
        if guess == v:
            result[i] = v
            print(result)
        chances += 1

print(result)