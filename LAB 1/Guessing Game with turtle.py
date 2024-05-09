#Guessing Game. Program generates a random integer and the player guesses the integer based on hints provided.
#initial version

import random #importing the random library
#Setting up the Variables

winning_number: 0
guess=0
no_of_guesses= int(0) #Setting it up to take in integer input
finished= False #Boolean operator to stop the game when the target score is reached.

winning_number=random.randint(1,100)

#Taking input from the User:
print(" I am thinking of a number. What number am I thinking of?")
guess=int(input("Please enter a number between 1 and 100: "))

no_of_guesses=no_of_guesses +1

while guess<0 or guess>100: #tried with if before, didn't iterate. While loop is better
    guess=int(input("Please enter a number between 1 and 100: "))

while finished== False: #Checks the condition if the game is over or not
    if guess>winning_number:
        print("Too high")
        guess=int(input("Please enter a number between 1 and 100: "))
        no_of_guesses= no_of_guesses + 1
    elif guess< winning_number:
        print("Too low")
        guess=int(input("Please enter a number between 1 and 100: "))
        no_of_guesses= no_of_guesses +1
    else:
        finished= True

print("You got it! My number is", str(winning_number))
print("It took you", str(no_of_guesses),"guesses to get the number!")
    
#Need to optimise it for better results.

"""
This was the initial version on idle interface. The thing here, is I needed multiple conditions.

"""
