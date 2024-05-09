# Done by ABID, Mohammed Sirajul Mostafa. SID: 20914532


import random               # Import the 'random' library
import turtle               # Import the "turtle" library
target = 0                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here
count=0                     # We will store the number of guesses here.
xposition= -150
yposition= 100

turtle.up()
#We will just change every print to turtle.write()
#We will change every input to turtle.textinput()

# Generate a new integer random number
target= random.randint(1,100)
turtle.goto(xposition, yposition)
turtle.write("I am thinking of a number. What number am I thinking of?", font=("Arial", 15, "bold"))
yposition=yposition - 40 #size is 20 so going to 40 is good. Moves turtle with next line.


# Do the main game loop
while not finished: #Using these logical operators act as better answers and better conditions.
    # Get the user's guess
    guess_input_text=turtle.textinput("Guessing Game","Please enter a number between 1 and 100: ") #textinput takes text input
    guess_input=int(guess_input_text)

    count= count + 1

    # Check the user's guess
    if guess_input<1 or guess_input> 100:
        turtle.goto(xposition, yposition)
        turtle.write("Please enter an integer number between 1 and 100. ", font=("Arial", 15, "bold"))
        yposition= yposition - 40
    elif guess_input> target:
        turtle.goto(xposition, yposition)
        turtle.write("Too high.", font=("Arial", 15, "underline"))
        yposition= yposition - 40
    elif guess_input< target:
        turtle.goto(xposition, yposition)
        turtle.write("Too low.", font=("Arial", 15, "bold"))
        yposition= yposition - 40
    else:
        finished= True
    

# At this point, the game is finished
turtle.goto(xposition, yposition)
turtle.write("You got it! My number is " + str(target) +".", font=("Arial", 15, "bold"))


#TypeError: can only concatenate str (not "int") to str
#The previous line was the error that was shown when I removed str() from str(target).
#You have to convert everything to string and concatenate them for turtle.write to work.

#notice how turtle.write(), you add strings together, ie concatenate them, instead of just separating them by comma.
#comma is used to add embellishments like font, fontsize and fontweight

"""
This print stuff can understand which is integer and which is string and it is able to give an output.
turtle.write() isn't able to do that. You need to concatenate all texts first and then, separate by comma to add fonts.

in python, the main texts are added by including
"""
yposition= yposition - 40
turtle.goto(xposition, yposition)
turtle.write("It took you " + str(count) + " guesses to get the number! ", font=("Arial", 15, "italic"))
yposition= yposition - 40



turtle.done()
