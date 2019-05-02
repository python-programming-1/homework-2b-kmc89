'''
For this assignment you'll make a rock paper scissors game!

git clone this repository like you did in homework-2a
create a file named rock_paper_scissors.py
Your program should print "make a move! (r/s/p)"
Your program should accept 6 inputs: 'r' for rock, 'p' for paper, 's' for scissors and 'y' for yes and 'n' for no, 'sc' for score.
Your program should randomly select a move. See https://docs.python.org/3/library/random.html for reference.
Your program should output the following line with one of the options (rock, paper, scissors) for the computer and yourself: 'You chose 'rock/paper/scissors' and the computer chose 'rock/paper/scissors'. You Win/Lose!
After a game, the computer should ask you 'Do you want to play again? (Y/N)?' If you enter 'y' the game should start over, if you enter 'n' the program should exit after saying "thanks bye!".
If a player inputs 'sc' return a score like: 'human: X, computer: Y'
Bonus: Can you make the computer smarter? Instead of a random move, have the computer make a move based on the player's history of moves. So if the player has played scissor three times, the computer may try to play rock.
Sample outp
'''
import random

again = "y"
humanScore = 0
computerScore = 0
userR = 0
userS = 0
userP = 0

while again == "y":

    while True:
        userInput = input("make a move! (r/s/p): ").lower()

        if userInput == "r" or userInput == "s" or userInput == "p":
            break
        
        print("Invalid input. Please try again!")
    
    userOutput = ""

    if userInput == "r":
        userOutput = "rock"      
    elif userInput == "s":
        userOutput = "scissors"
    elif userInput == "p":
        userOutput = "paper"
   
    # computer will react if human plays three same move in a row!
    if userS >= 3:
        autoMove = 1
    elif userR >= 3:
        autoMove = 3
    elif userP >= 3:
        autoMove = 2
    else:
        autoMove = random.randint(1,3)
    
    autoOutput = ""
    # 1 = rock  2 = scissors  3 = paper
    if autoMove == 1:
        autoOutput = "rock"
    elif autoMove == 2:
        autoOutput = "scissors"
    elif autoMove == 3:
        autoOutput = "paper"

    outcome = ""

    if userInput == "r":
        if autoMove == 1:
            outcome = "You tie"
        elif autoMove == 2:
            outcome = "You win"
            humanScore += 1
        elif autoMove == 3:
            outcome = "You lose"
            computerScore +=1

    if userInput == "s":
        if autoMove == 1:
            outcome = "You lose"
            computerScore += 1
        elif autoMove == 2:
            outcome = "You tie"
        elif autoMove == 3:
            outcome = "You win"
            humanScore += 1

    if userInput == "p":
        if autoMove == 1:
            outcome = "You win"
            humanScore += 1
        elif autoMove == 2:
            outcome = "You lose"
            computerScore += 1
        elif autoMove == 3:
            outcome = "You tie"

    print("You chose '" + userOutput + "' and the computer chose '" + autoOutput + "'. " + outcome + "!")

    # reocrd of human play
    if userInput == "r":
        userR += 1
        userS = userP = 0
    elif userInput == "s":
        userS += 1
        userR = userP = 0
    elif userInput == "p":
        userP += 1
        userR = userS = 0

    while True:
        again = input("Don you want to play again (Y/N) ?").lower()

        if again == "sc":
            print("human: " + str(humanScore) + "; computer: " + str(computerScore))
            continue

        if again == "y" or again == "n":
            break
        print("Invalid input. Please try again!")

print("Thanks bye!")