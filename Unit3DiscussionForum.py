import random

#First I will declare some variables to compare for my conditionals
MyWinStreak = random.randint(0,3) #random number between 0 and 3
ThreeWinStreak = 3
TwoWinStreak = 2
WonLastGame = 1

#Here is an example function showing chained conditional:
def CheckWinsViaChainedConditional(MyWinStreak):
    if MyWinStreak == ThreeWinStreak:
        print("You have won three games in a row!")
    elif MyWinStreak == TwoWinStreak:
        print("You have won two games in a row!")
    elif MyWinStreak == WonLastGame:
        print("You have won your last game.")
    else:
        print("You lost your last game.")

#Here is the same logic from the previous function, except in a nested conditional format:
def CheckWinsViaNestedConditional(MyWinStreak):
    if MyWinStreak == ThreeWinStreak:
        print("You have won three games in a row!")
    else:
        if MyWinStreak == TwoWinStreak:
            print("You have won two games in a row!")
        else:
            if MyWinStreak == WonLastGame:
                print("You have won your last game.")
            else:
                print("You lost your last game")

#Now I will call both versions
print("Chained conditional test:")       
CheckWinsViaChainedConditional(MyWinStreak)
print("Nested conditional test:")
CheckWinsViaNestedConditional(MyWinStreak)