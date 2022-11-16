import random
name=input("give me everybody's name and seperated by a comma:")
name_list=name.split(",")
random_choose_ppl=random.randint(0,len(name_list)-1)
choose_ppl=name_list[random_choose_ppl]
print(choose_ppl+ "is going to pay the bill for today")
game_List=["rock", "paper", "scissor"]
user_choose=int(input("what do you choose? type 0 for Rock, 1 for Paper and 2 for Scissor\n"))
if user_choose>=3 or user_choose<0:
    print("this is an invaild number,you lose!")
else:
    print(game_List[user_choose])
    computer_choose=random.randint(0,2)
    print("computer choose:")
    print(game_List[computer_choose])
    if computer_choose==0 and user_choose==2:
        print("You lose!")
    elif computer_choose<user_choose:
        print("You win!")
    elif computer_choose==user_choose:
        print("this is a draw!")
    elif computer_choose==2 and user_choose==0:
        print("You lose!")
    elif computer_choose>user_choose:
        print("You lose!")
    else:
        print("this is an invaild number, you lose!")


