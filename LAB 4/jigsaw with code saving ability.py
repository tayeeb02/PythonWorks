#Done by ABID, Mohammed Sirajul Mostafa, 20914532

import turtle
import random
    
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image
def createJigsaw():
    global allTurtles

    # Initialize the variables of total number of rows and columns
    totalRows=5
    totalColumns=5
    
    # Now we go through the jigsaw piece row-column structure
    # Go through each row
    for row in range(totalRows):
        # Go through each column in this row
        for col in range(totalColumns):
            # Generate a random position
            x_pos= random.randint(-int(turtle.window_width()/2),int(turtle.window_width()/2))
            y_pos= random.randint(-int(turtle.window_height()/2),int(turtle.window_height()/2))
            # Make a new turtle
            newTurtle=turtle.Turtle()
        
            # Move it to the random position
            newTurtle.up() #Careful about the turtle you selected.
            newTurtle.speed(0)
            newTurtle.goto(x_pos, y_pos)
            
            # Build the image file name
            theFilename= "image-" + str(row) + "-" + str(col) +".gif"
            #print(theFilename) #checking if the filename is correct. 
            
            # Add the image to the turtle system
            turtle.addshape(theFilename)
            # Apply the new image to this turtle
            newTurtle.shape(theFilename)
            # Now fix it so that when this turtle is dragged, it goes to the place where it is dragged
            newTurtle.ondrag(newTurtle.goto) 
            # Add the new turtle to the new list of turtles
            allTurtles.append(newTurtle)


        
### This part of Python code will only run when the user presses "c" to check the jigsaw
def checkJigsaw():
    checkResult=True # At the start, we assume everything is OK

    for thisTurtle in allTurtles: # Go through every single turtle that we made
        thisX = thisTurtle.xcor() # Get the x coordinate of this turtle
        thisY = thisTurtle.ycor() # Get the y coordinate of this turtle
        
        # An example filename is "image-2-1.gif"
        theFilename = thisTurtle.shape() # Take the image filename of this turtle
        
        lengthOfFilenameWithoutExtension= len(theFilename)-4 # How long the filename is without the ".gif"
        theFilenameWithoutExtension=theFilename[ : lengthOfFilenameWithoutExtension ] # Remove the ".gif"
        FilenameWithoutExtension=theFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

        thisRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
        thisCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
        
        thisRow=int(thisRow) # Have to convert the text to an integer before comparing it with a number
        thisCol=int(thisCol) # Have to convert the text to an integer before comparing it with a number

        # We need to check this turtle with all other turtles for position violations
        for compareTurtle in allTurtles: # Go through every other turtle
            compareX = compareTurtle.xcor() # Get the x coordinate of the turtle
            compareY = compareTurtle.ycor() # Get the y coordinate of the turtle
            
            # An example filename is "image-2-1.gif"
            compareFilename = compareTurtle.shape() # Take the image filename of this turtle
            
            lengthOfCompareFilenameWithoutExtension= len(compareFilename)-4 # How long the filename is without the ".gif"
            compareFilenameWithoutExtension=compareFilename[ : lengthOfCompareFilenameWithoutExtension ] # Remove the ".gif"
            FilenameWithoutExtension=compareFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

            compareRow=FilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
            compareCol=FilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
            
            compareRow=int(compareRow) # Have to convert the text to an integer before comparing it with a number
            compareCol=int(compareCol) # Have to convert the text to an integer before comparing it with a number

            # Here, the four position violations will be checked
            # The jigsaw is wrong if any of them fails
            
            # The piece has a smaller column value but is on the right
            if thisCol < compareCol and thisX >= compareX:
                checkResult = False
                break

            # The piece has a larger column value but is on the left
            if thisCol > compareCol and thisX <= compareX:
                checkResult = False
                break
            
            # The piece has a smaller row value but is on the bottom
            if thisRow < compareRow and thisY <= compareY:
                checkResult = False
                break
            
            # The piece has a larger row value but is on the top
            if thisRow > compareRow and thisY >= compareY:
                checkResult = False
                break
            
            
    # Let's check the final result and show an appropriate message
    turtle.up()
    turtle.goto(-200,-300)
    turtle.hideturtle()
    
    if checkResult:
        turtle.clear()
        turtle.write("Congratulations! Your jigsaw is correct!", font=("Arial", 20,"bold"))
    else:
        turtle.clear()
        turtle.write("Oh no! Your jigsaw is WRONG!!", font=("Arial", 20, "bold"))

#The following code acts as the save button in game, writes the names of the stored locations.

def SavePosition():
    filename = turtle.textinput("Save your jigsaw positions", \
                                "What is the jigsaw filename you want to create?")
    myfile = open(filename, "wt") #This is basically writing mode. wt. Notice it must be in inverted commas.

    #Go through each turtle in list of turtles.

    for thisTurtle in allTurtles:

        #make a string of one turtle, in the right format.
        #Here we will take x position, then separated by tab, then y position, with new line character
        #The new line character will become useful soon.
        #Just note that these special characters must be inside quotation marks.
        one_line= str(thisTurtle.xcor())+ "\t" + \
                  str(thisTurtle.ycor()) + "\n"

        #Save string to fiile.
        myfile.write(one_line)
    # Close the file
    myfile.close()

#The next function will read the files, extracting information and asking turtles to shift to those particular location.
#Why might it work? Because when writing the file, we wrote it in order of indices of turtles.
"""
whitespace is anything you can't see
That includes spaces and end of line characters.
What it does basically after the last non space character, it will remove all the white spaces

we use variable_name.rstrip() method to remove whitespace.
rstrip() means remove anything you can't see on the right side.
Possibly, we can use it on the left side as well. Perhaps lets test it out sometime? Might be useful
"""

#Both Save and Load functions work beautifully. Using functions is more convenient because
#If you don't know which part of the code to place them in, you can create a separate function and just stick it in whenever you need it,
#You don't have to write such codes for everything


def LoadPosition(): #Note because we are using keypresses, the function does not need to have parameters.

    """
     NOTE: split() function is used to strip a string of letters at different locations separated by a character.

     Example I have:text= this-is-just-a-test-theory-for-string.
     items= text.split("-")
     now, items becomes a list containing [this, is, just, a, test, theory, for, string]

     
     
    """
    filename= turtle.textinput("Load jigsaw positions", \
                               "What is the jigsaw filename you want to load?")
    myfile= open(filename, "r") #This r means in read mode. you can't write in this mode

    turtleIndex=0
    for line in myfile: #Forces to look through every line, so your code can work for any number of jigsaw pieces
        #handle each line one by one
        line = line.rstrip() #This removes the newline character
        items= line.split("\t") #Notice in the code that the x and y coordinates were separated by tab character

        x= float(items[0]) #Convert x to float
        y= float(items[1]) #Convert y to float So you get exact location

        allTurtles[turtleIndex].goto(x,y)
        turtleIndex=turtleIndex + 1

        #The last 2 lines of codes were amazing. It guides position of turtle for each turtle, saving a lot of memory in the process

    myfile.close()
            
    

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces

#print(allTurtles) -Testing what happens after adding, if they were added correctly or not. 
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.onkeypress(SavePosition, "s")

turtle.onkeypress(LoadPosition, "l")

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
#turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate

#Hmm, removing it still didn't make a difference. 
