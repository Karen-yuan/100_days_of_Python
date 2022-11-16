print("Welcome to Treasure Island, your mission is to find the treasure!")
first_task=input('You are at a crossroad, where do you want to go? Type "left" or "right"\n').lower()
if first_task=="left":
    sec_task=input('When you came across a river in the middle of the island, will you choose to "swim" or "wait"?\n').lower()
    if sec_task=="wait":
        third_task=input('Here is the last choose:there are three big doors in front of you, will you choose the "red" or the "blue" or the "yellow"?\n').lower()
        if third_task=="yellow":
            print("Congrats you found the treasure! You win!")
        else:
            print("There is a monster inside the door, game over.")
    else:
         print("Opps you are unforunately drowned, game over")
else:
     print("You fell into a hole,game over")
    










