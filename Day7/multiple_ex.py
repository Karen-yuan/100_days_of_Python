# random word exercise:
import random
word_list = ["ardvardk", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}.")

# guess letter game
display = []
word_lengh = len(chosen_word)
for _ in range(word_lengh):
    display = display+"_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess a letter:").lower()
for position in range(word_lengh):
    letter = chosen_word[position]
    print(
        f"Current position: {position}\n Current letter:{letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)
if "_" not in display:
    end_of_game = True
    print("You win.")
