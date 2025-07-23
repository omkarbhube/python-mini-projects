import random
user_choice = int(input("Enter 0 for Rock  1 for Paper  2 for Scissor: "))
comp_choice = random.randint(0,2)
# 0 - Draw, 1 - Win, 2 - Lose
possibilities = [
                 [0,2,1],
                 [1,0,2],
                 [2,1,0]
 ] 
if possibilities[user_choice] [comp_choice] == 0:
    print("Draw")
elif possibilities[user_choice] [comp_choice] == 1:
    print("You Wins!")
elif possibilities[user_choice] [comp_choice] == 2:
    print("You Lose!")
else:
    print("Invalid Input")