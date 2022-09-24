# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
play = "y"

while (play == "y"):

    choice = input('Player 1, input your choice rock, paper, scissors (1 = rock, 2 = paper, 3 = scissors)' )
    choice2 = input('Player 2, input your choice rock, paper, scissors (1 = rock, 2 = paper, 3 = scissors)')
    
    draw = "y"
    
    while (choice == choice2) and (draw == "y"):
        draw = input("Draw!, Do you want to continue playing? (y/ n)")
        if (draw == "n"):
            break
        else: 
            choice = input('Player 1, input your choice rock, paper, scissors (1 = rock, 2 = paper, 3 = scissors)' )
            choice2 = input('Player 2, input your choice rock, paper, scissors (1 = rock, 2 = paper, 3 = scissors)')
            
    if (choice == "1") and (choice2 == "2"):
        print("player 2 wins")
    elif (choice == "2") and (choice2 == "3"):
        print ("player 2 wins")
    elif (choice == "3") and (choice2 == "1"):
        print ("player 2 wins")
    elif (choice == "2") and (choice2 == "1"):
        print("player 1 wins")
    elif (choice == "3") and (choice2 == "2"):
        print ("player 1 wins")
    elif (choice == "1") and (choice2 == "3"):
        print ("player 1 wins")
    else:
        print ("nobody wins")
        
    play = input("do you want to play again? (y/n)")