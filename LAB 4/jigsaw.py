import turtle
import random
    
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image
def createJigsaw():
    global allTurtles

    # Initialize the variables of total number of rows and columns
    
    # Now we go through the jigsaw piece row-column structure
    # Go through each row
        # Go through each column in this row
            # Generate a random position

            # Make a new turtle
            
            # Move it to the random position

            # Build the image file name
            
            # Add the image to the turtle system
            # Apply the new image to this turtle
 
            # Now fix it so that when this turtle is dragged, it goes to the place where it is dragged
             
            # Add the new turtle to the new list of turtles

        
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
            
            # The piece has a smaller row value but is on the bottom
            
            # The piece has a larger row value but is on the top
            
            
    # Let's check the final result and show an appropriate message
    if checkResult:
        print("Congratulations! Your jigsaw is correct!")
    else:
        print("Oh no! Your jigsaw is WRONG!!")

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate

