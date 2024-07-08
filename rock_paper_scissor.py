import random

computer_wins = 0
player_wins = 0
count = 0

options = ["rock", "paper", "scissors" ,"q"]

while True:
    count += 1
    if count == 1:
        playerPick = input("Welcome to rock, paper, scissors,type your pick or q to quit: ").lower()

    if count > 1:
        print("Round", count,":")
        playerPick = input("Type your pick or q to quit: ").lower()


    if playerPick not in options:
        print("Invalid pick, try again")

    if playerPick == "q":
        quit()

    randnumber = random.randint(0 , 2)
    computer_pick = options[randnumber]

    if playerPick == computer_pick:
        print("Draw,Computer choice was also", computer_pick)
        continue
    elif playerPick == "rock" and computer_pick == "paper":
        player_wins += 1
        print("You win")
        print("Your score is", player_wins ,",Computer Score is", computer_wins ,",Computer chose", computer_pick)
        continue
    
    elif playerPick == "paper"  and computer_pick == "rock":
        player_wins += 1
        print("You win")
        print("Your score is", player_wins ,",Computer Score is", computer_wins ,",Computer chose", computer_pick)
        continue
        
    
    elif playerPick == "scissors" and computer_pick == "paper":
        player_wins += 1
        print("You win")
        print("Your score is", player_wins ,",Computer Score is", computer_wins ,",Computer chose", computer_pick)
        continue

    else:
        computer_wins += 1
        print("You Lost,The Computer chose", computer_pick)
        print("Your score is", player_wins ,"Computer Score is", computer_wins)
        continue
