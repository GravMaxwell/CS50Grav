import sys
import random

def get_positive_integer(prompt):
    while True:
        try:
            # prompt user for input and format as integer
            value = int(input(prompt))

            if value > 0:
                return value
        except ValueError:
            # ignore error if users input is not an integer
            pass

def main():
    level = get_positive_integer("Level: ")
    target = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("too large!")
        else:
            print("Just right!")
            sys.exit() # end loop if user guesses correctly (not sure why break did not exit the program fast enough but sys exit did !)

main()
