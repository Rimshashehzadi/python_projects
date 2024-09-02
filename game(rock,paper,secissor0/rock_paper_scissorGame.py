"""
WORKFLOW OF PROJECT:
1- Input from user(Rock,Paper,Scissor)
2- Computer choice (Computer will choose randomly nor conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random

item_list = ['Rock','Paper','Scissor']

user_choice = input("Enter you move = Rock, Paper, Scissoe = ")

#randomly select item form item_list
com_choice = random.choice(item_list)

print(f"User choice  {user_choice} Computer choice = {com_choice}")
 
 # print result with randomly enter user value and win as soon as possible
if user_choice == com_choice:
    print("Both chooses same: = Match tie")

elif user_choice == 'Rock':
    if com_choice == 'Paper':
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")
elif user_choice =='Paper':
    if com_choice == 'Scissor':
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock,You Win")
elif user_choice == 'Scissor':
    if com_choice == 'Paper':
        print("Scissor cuts paper,You Win")
    else:
        print("Rock smashes scissor,Computer Win")                    


