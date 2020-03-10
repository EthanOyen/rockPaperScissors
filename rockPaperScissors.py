'''
Created on Feb 29, 2020

@author: ITAUser
'''
#Pseudocode:
#set variable keepPlaying to True
#while variable keepPlaying is True
#    print statement welcoming players to the game
#    print statement stating the rules (best 2 out of 3, press q to quit)
#    make a key that assigns a number to each choice for the computer
#
#    import the random function
#    set computer's score to 0
#    set player's score to 0
#
#    while player's score is less than 2 and computer's score is less than 2
#
#        computer's choice = random number between 1 and 3
#        player's choice = input(ask player to select rock, paper, or scissors)
#
#        start checking user options
#        if player inputs 'q'
#
#            set keepPlaying to False
#            stop the loop (break)
#
#        else if (player inputs rock and computer chooses rock) or
#        (player inputs paper and computer chooses paper) or
#        (player inputs scissors and computer chooses scissors)
#
#            print out DRAW
#            print out player's score and computer's score
#
#        else if (player inputs rock and computer chooses scissors) or
#        (player inputs paper and computer chooses rock) or
#        (player inputs scissors and computer chooses paper)
#
#            add one to player score
#            print out player's score and computer's score
#
#        else if (player inputs rock and computer chooses paper) or
#        (player inputs paper and computer chooses scissors) or
#        (player inputs scissors and computer chooses rock)
#
#            add one to the computer's score
#            print out player's score and computer's score
#
#        else
#
#            tell the user their input wasn't valid
#
#    print statement thanking the players for playing
#    if player's score is 2:
#
#        print statement letting player know they won
#
#    if computer's score is 2:
#
#        print statement letting the player know the computer won
#
#    print out player's score and computer's score




import random
 
keepPlaying = True
while keepPlaying == True:
    print("Welcome to Rock, Paper, Scissors\nBest 2 out of 3 wins.\n Press Q to quit.\n")
    key = ["rock", "paper", "scissors"]
    situations = ["Draw", "Player wins round", "Computer wins round"]
    addToScore = [[0, 1, 0], [0, 0, 1]]
    playerScore = 0
    compScore = 0
 
    while playerScore < 2 and compScore < 2:
        compChoice = random.randint(0,2)
        userChoice = input("Rock, Paper, or Scissors?\n").lower()
 
        try:
            playerChoice = key.index(userChoice)
        except:
            playerChoice = 10
 
        if userChoice == 'q':
            keepPlaying = False
            break
  
        elif userChoice == 10:
            print("Invalid Input")
            break
 
        winner = playerChoice - compChoice
        playerScore += addToScore[0][winner]
        compScore += addToScore[1][winner]
        print("Player chose: " + str(userChoice))
        print("Computer chose: " + key[compChoice])
        print(situations[winner])
        print("Player: " + str(playerScore))
        print("Computer: " + str(compScore))
        print()
 
    print("Thanks for playing!")
 
    if(keepPlaying == False):
        break
 
    elif playerScore > compScore:
        print("Congratulations, you win!")
 
    else:
        print("Sorry, you lose")
 
print("Final Score:")
print("Player: " + str(playerScore))
print("Computer: " + str(compScore))
print()