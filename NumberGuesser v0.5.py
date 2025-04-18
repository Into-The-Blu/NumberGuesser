import random
import sys
#import json 
#import os

scoreboard = []

#requests user input to decide the difficulty. 
#each case returns a number of chances, and assigns a score multiplier to the diff variable
def getDiff():
    print(f"\nWhat difficulty would you like to play on?\n1. Easy (10 guesses)\n2. Medium (5 guesses)\n3. Hard (3 guesses)")
    global diff
    while True:
        match str(input(f"\nInput:").lower()):
            case "easy"|"1":
                diff = 1.0
                return 10
            case "medium"|"2":
                diff = 1.25
                return 5
            case "hard"|"3":
                diff = 3.0
                return 3
            case _:
                print("I didn't recognise that input, could you retype?")
                continue

#main game body - main loop repeats for each guess, and is only broken by a win or lose condition
#if-elif-else statements react to the user guessing correctly, wrong and above, or wrong and below
def guesrBody():
    chances = getDiff() #outputs no. of chances based on user difficulty input
    number = random.randint(1,100)
    print(f"\nAlright! Make your first guess.\n")
    for i in range(chances):
        x = int(input(f"\nInput:").strip())
        if x == number: #checks for a win condition
            global score
            score = ((chances-(i+1))/chances)*100*diff #(chances left/total chances)*100*difficulty multiplier
            score = int(round(score))
            scoreboardCalc()
            if i + 1 == 1:
                print(f"\nWell done! It only took you {i+1} guess! Your score is:{score}")
            else:
                print(f"\nWell done! It took you {i+1} guesses! Your score is:{score}")
            global gameFinished
            gameFinished = True
            menu()
            break
        elif x > number: #checks for a wrong and above
            if chances - (i+1) > 1:
                print(f"Too high! You have {chances-(i+1)} attempts left.\n")
            else: 
                print(f"Too high! You only have {chances-(i+1)} attempt left!\n")
        else: #checks for a wrong and below
            if chances - (i+1) > 1:
                print(f"Too low! You have {chances-(i+1)} attempts left.\n")
            else:
                print(f"Too low! You only have {chances-(i+1)} attempt left!\n")
    if gameFinished == True:
        pass
    else: 
        print(f"Uh oh! You've run out of attempts.")
        menu()

#gives the user 3 options: new game, scoreboard, and exit. responds to user input
def menu():
    print(f"\nWhat would you like to do?\n\nMenu:\n1. New Game\n2. View Scoreboard\n3. Exit")
    while True:
        match str(input(f"\nInput:")):
            case "1": #starts the game
                guesrBody()
            case "2": #displays scoreboard
                print(f"\nScoreboard:\n-----------")
                for i in range(len(scoreboard)):
                    print(f"{i + 1}.  {scoreboard[i]}")
                if len(scoreboard) == 9:
                    print(f"10. {scoreboard[9]}")
                print("-----------")
                break
            case "3": #exits game
                print("Thank you for playing! Enter any input to exit.")
                if input() == True:
                    sys.exit()
            case _:
                print("I didn't recognise that input, could you retype?")
                continue
    menu()        

#inserts score into scoreboard, then trims index to 10 if >10 
def scoreboardCalc():
    scoreboard.append(score)
    scoreboard.sort(reverse = True)
    if len(scoreboard) >= 11:
        del scoreboard[10]

#program push-off point
print(f"Welcome to my Number Guessing Game!\nI will think of a number between 1 and 100, and you have a set amount of chances to guess it.")
menu()

