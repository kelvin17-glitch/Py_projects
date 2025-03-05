import random
import math
import time

def slow_print(text, delay=0.09):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

slow_print("---Hi! Wanna Play a Game??:)---")
res = input("Y/n? ").lower()

if res == "y":
    # Get input range
    slow_print("Yaay! I'm a computer so I love numbers. Give me a range?")
    user_range = input("Enter a range(Format--> Lower-Upper): ")
    range_mod = user_range.split("-")

    # Compiler guess
    comp_guess = random.choice(range(int(range_mod[0]), int(range_mod[1])+1))

    # Initialize max number of turns
    max_turns = int(math.log2(int(range_mod[1])))

    # Let the games begin
    slow_print("I'm gonna think of a number in the range. Can you guess it?")
    slow_print(f"You get {max_turns} turns. Make 'em count!")
    turns = 0
    while turns < max_turns:
        if (max_turns - turns) == 1:
            # On the last turn
            slow_print("Last chance! Give it your best shot:)")
            guess = int(input("Which number I'm I thinking of? "))
            
            if guess == comp_guess:
                slow_print("You must be psychic! You got it!!")
                break
            elif guess > comp_guess:
                slow_print("That's too high! You lose!")
            elif guess < comp_guess:
                slow_print("That's too low! You lose!")
        else:
            guess = int(input("Which number I'm I thinking of? "))
            if guess == comp_guess:
                slow_print("You must be psychic! You got it!!")
                break
            elif guess > comp_guess:
                slow_print("That's too high! Guess again!")
            elif guess < comp_guess:
                slow_print("That's too low! Guess again!")

        turns += 1
elif res == "n":
    slow_print("Then why tf did you run this file, dumbass?")
else:
    slow_print("Oh Brother! You must be dumb af!")

