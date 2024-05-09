import random               # Import the 'random' library

target = 0                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here
count=0                     # We will store the number of guesses here.

# Generate a new integer random number
target= random.randint(1,100)
print("I am thinking of a number. What number am I thinking of?")


# Do the main game loop
while not finished:
    # Get the user's guess
    guess_input_text=input("Please enter a number between 1 and 100: ")
    guess_input=int(guess_input_text)

    count= count + 1

    # Check the user's guess
    if guess_input<1 or guess_input> 100:
        print("Please enter an integer between 1 and 100: ")
    elif guess_input> target:
        print("Too high.")
    elif guess_input< target:
        print("Too low.")
    else:
        finished= True

"""
while not finished or while true ie boolean conditions are there if you want an indefinite amounts of repetition


"""
    

# At this point, the game is finished
print("You got it! My number is " + str(target) +".")
print("It took you " + str(count) + " guesses to get the number! ")
