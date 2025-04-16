import random
import sys
#import json
#import os

scoreboard = []

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

def guesrBody():
    chances = getDiff()
    number = random.randint(1,100)
    print(f"\nAlright! Make your first guess.\n")
    for i in range(chances):
        x = int(input(f"\nInput:").strip())
        if x == number:
            global score
            score = ((chances-(i+1))/chances)*100*diff
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
        elif x > number:
            if chances - (i+1) > 1:
                print(f"Too high! You have {chances-(i+1)} attempts left.\n")
            else: 
                print(f"Too high! You only have {chances-(i+1)} attempt left!\n")
        else:
            if chances - (i+1) > 1:
                print(f"Too low! You have {chances-(i+1)} attempts left.\n")
            else:
                print(f"Too low! You only have {chances-(i+1)} attempt left!\n")
    if gameFinished == True:
        pass
    else: 
        print(f"Uh oh! You've run out of attempts.")
        menu()

def menu():
    print(f"\nWhat would you like to do?\n\nMenu:\n1. New Game\n2. View Scoreboard\n3. Exit")
    while True:
        match str(input(f"\nInput:")):
            case "1":
                guesrBody()
            case "2":
                print(f"\nScoreboard:\n-----------")
                for i in range(len(scoreboard)):
                    print(f"{i + 1}.  {scoreboard[i]}")
                if len(scoreboard) == 9:
                    print(f"10. {scoreboard[9]}")
                print("-----------")
                break
            case "3":
                print("Thank you for playing! Enter any input to exit.")
                if input() == True:
                    sys.exit()
            case _:
                print("I didn't recognise that input, could you retype?")
                continue
    menu()        

def scoreboardCalc():
    scoreboard.append(score)
    scoreboard.sort(reverse = True)
    if len(scoreboard) >= 11:
        del scoreboard[10]

print(f"Welcome to my Number Guessing Game!")

menu()

