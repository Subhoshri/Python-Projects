import random
import time

def choose():
    lis=[scissor,rock,paper]
    comp=random.choice(lis)
    return comp

#unicode symbols
scissor=u"\u270C"
rock=u"\U0001F44A"
paper=u"\U0001F590"

print("Welcome to Rock-Paper-Scissors Game\n\nThe Rules are simple:\nRock beats Scissor\nScissor beats Paper\nPaper beats Rock"
      "\n\nThe one who first reaches the score of 5 is the winner.")

round=1
score=0
comp_score=0

while True:
    time.sleep(1)
    print("\nRound {}:\n".format(round))
    #taking user input
    user=input("Choose Rock, Paper or Scissors(or R, P, S): ")
    comp=choose()
    if user.lower()=="scissors" or user.lower()=='s':
        user=scissor
    elif user.lower()=="rock" or user.lower()=='r':
        user=rock
    elif user.lower()=="paper" or user.lower()=='p':
        user=paper
    else:
        print("Wrong Input! Try Again")
        continue

    round+=1
    
    print("Your Choice: {}      Computer's Choice: {}".format(user,comp))
    #calculating the winner
    flag=0
    if comp==scissor:
        if user==paper:
            flag=1
        elif user==rock:
            flag=2
    elif comp==rock:
        if user==scissor:
            flag=1
        elif user==paper:
            flag=2
    else:
        if user==rock:
            flag=1
        elif user==scissor:
            flag=2
    
    if flag==0:
        print("It's a Tie!")
    elif flag==1:
        print("Oops! The computer wins")
        comp_score+=1
    else:
        print("Yay! You won!")
        score+=1

    if score==5 or comp_score==5:   #score reached or not
        break

for i in range(3):
  print("Calculating score"+"."*i,end="\r")
  time.sleep(1)

print("\nFinal Scores:\nYou: {}         Computer: {}\n".format(score,comp_score))
if score>comp_score:
    print("Congratulations, You Won This Game!")
else:
    print("The Computer Won This Game. Better Luck Next Time!")
  
