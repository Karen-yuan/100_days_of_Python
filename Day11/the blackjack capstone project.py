import random
import os


def deal_card():
    # return a random card from the deck''''''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card\



def calculate_score(cards):
    # take a list of cards and return the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw🙃️"
    elif computer_score == 0:
        return "Lose, opponent has blackjack🕶️"
    elif user_score == 0:
        return "Win with a blackjack🕶️"
    elif user_score > 21:
        return "opponent went over, you lose😭"
    elif computer_score > 21:
        return "Opponent went over, you win😄"
    elif user_score > computer_score:
        return "You win😄"
    else:
        return "You lose😫"


# deal the user and the computer 2 cards each using deal_card()
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(deal_card())

    while not is_game_over:
        # this while loop is for the user so that they could continue taking cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your card is {user_cards}, and your score is{user_score}")
        print(f" computer first card is {computer_cards[0]}")
    # call the calculte_score (),and if the computer or the user has a blackjack (0)or if the user's score is over 21, then the game is over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "type 'y' to get another card and type 'n' to pass")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        # this while loop is for the computer to continue draw cards
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand:{user_cards},your final score :{user_score}")
    print(
        f"computer's final hand:{computer_cards}, and final score :{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y'or 'n' :") == 'y':
    os.system("clear")
    play_game()
