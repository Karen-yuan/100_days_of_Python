from game_data import data
# generate random data from the game data.
import random
# format the acount data into printable format by using function and then call it later.
import os


def format_data(account):
    # take the acocunt data and returns the printable format
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_description},from{account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers and guess == "a":
        return True
    elif a_followers > b_followers and guess == "b":
        return False
    elif a_followers < b_followers and guess == "a":
        return False
    else:
        return True

    "take the user guess and follower counts and returns if they got it right"


score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue == True:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(f"Compare B:{format_data(account_b)}")
    # ask the user to guess and check the answer.
    sum = 0
    user_guess = input(
        "who do you think have more followers in instagram? choose 'A'or'B'").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # give user feedback on their guess.
    # score keeping.
    if is_correct == True:
        score = score+1
        print(f"you are right! and your current socre is{score}")
        os.system("clear")
    else:
        game_should_continue = False
        print(f"sorry, that's wrong. and your final score is {score} ")
    # make the game repeatable(think about while loop------make account positionB became positionA.

    # clear the screen.


# print(account_b)
# print(account_a)
