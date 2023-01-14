from random import randint
#create a list of play options
t = ["rock", "paper", "scissors"]
#assign a random play to the computer
computer = t[randint(0,2)]
#set player to False
player = False
while player == False:
#set player to True
    player = input("rock, paper, scissors?")
    if player == computer:
        print("it's a tie! :]")
    elif player.lower() == "rock":
        if computer == "paper":
            print("you lose! :(", computer, "covers", player)
        else:
            print("you win! :)", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("you lose! :(", computer, "cut", player)
        else:
            print("you win! :)", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("you lose! :(", computer, "smashes", player)
        else:
            print("you win! :)", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]