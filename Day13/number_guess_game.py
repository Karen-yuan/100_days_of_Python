# choose a difficulty: either easy or difficult
# store a random correct number into a variable
# use for loop (two ,one for easy,one for diff)to let the users to guess number.
#       Also inside the loop, using guess_number to store the input number.
#       each time the loop runs, check does the input match to the correct number or not
#       if the number was not match, there is two occasions, if it is <input_number,then print too low\n,guess again, if ot is >input_number, then print too high, guess again
#       if it is match, then print "you got it, and you guess the right number"out
#       if it is use the chance up and still not match, then print"you lose,you run out of the guesses"
#       also track the number of turns and reduce it by 1 if they get it wrong
#

from random import *
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
game_level = input("choose a difficulty. type 'easy'and 'hard': ")
correct_number = randint(1, 100)
#print(f"pssst, the correct answer was {correct_number}")
if game_level == 'hard':
    print("you have 5 attempts remaining to guess the number")
    for guess_number in range(0, 5):
        guess_number = int(input("make a guess"))
        if guess_number < correct_number:
            print("too low.\nguess it again. ")
        elif guess_number > correct_number:
            print("too high.\nguess it again. ")
        else:
            print("you got it.\n that is correct.\n you win!")
    print("you lose\n you run out of the guesses")

elif game_level == "easy":
    print("you have 10 attempts remaining to guess the number")
    for guess_number in range(0, 10):
        guess_number = int(input("make a guess"))
        if guess_number < correct_number:
            print("too low.\n guess it again. ")
        elif guess_number > correct_number:
            print("too high.\n guess it again. ")
        else:
            print("you got it.\n that is correct.\n you win!")
    print("you lose\n you run out of the guesses")

else:
    print("there is no such option here, choose again ")
