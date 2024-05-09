# COMP1021 Lab 2 Python Sketchbook
# Name: ABID, Mohammed Sirajul Mostafa
# Student ID: 20914532
# Email: msmabid@connect.ust.hk

import turtle       # Import the turtle module for the program
import random

turtle.width(4)
turtle.speed(0)

##### Initialize the colour
fillcolor = "black"
turtle.pencolor("black")
turtle.fillcolor(fillcolor)

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        # Asking user for inputting the angle
        angle= input("Please enter the angle of rotation: ")
        angle=int(angle)
        
        #rotating the turtle
        turtle.left(angle) 

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        # asking user for height and width
        width= input("Please enter the width of the rectangle: ")
        width=int(width)
        height=input("Please enter the height of the rectangle: ")
        height=int(height)
        
        #drawing the rectangle
        turtle.begin_fill()
        for i in [0,1]: #This is basically repeating 2 times but it uses in. This is better, you can customise stuff.
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill() 

    ##### Handle the circle option
    if option == "c":
        print()

        #taking input of radius from user
        radius= input("Please enter the radius of the circle: ")
        radius= int(radius)
        
        #Drawing the circle
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

    ##### Handle the pen colour option
    if option == "p":
        print()

        #Asking user for color of the pen
        color= input("Please enter a colour name for the pen colour: ")
        color= str(color)
        
        #changing the color
        turtle.pencolor(color)

    ##### Handle the fill colour option
    if option == "f":
        print()

        #Taking input of fill colour from user
        fillcolor= input("Please enter a colour name for the fill colour: ")
        
        #Changing the color
        turtle.fillcolor(fillcolor)

    ##### Handle a generated flower
    if option == "g":
        print()

        #Taking input the size of flower
        size = input("Please enter the size of the flower petal: ")
        size= int(size)
        turtle.speed(2)
        #Drawing the flower
        for i in range(int(360/12)): #This basically controls what kind of flower you want
            for j in range(3):
                turtle.forward(size)
                turtle.left(120)
            turtle.left(12)

    ##### Handle a generated explosion
    if option == "e":
        print()

        dotSize= input("Please input the size of explosion (>150): ")
        dotSize= int(dotSize)
        while dotSize>=10:
            for thiscolor in ["yellow","turquoise","SteelBlue","LightSteelBlue",
                              "DodgerBlue","DeepSkyBlue", "chocolate", "azure"]:

                for j in range(1,5):
                    drawColor= thiscolor + str(j)
                    turtle.color(drawColor)
                    turtle.dot(dotSize)
                    dotSize= max(dotSize-10,0) #Prevent program from crashing because the dots would be too small.
                 

    ##### Handle author information drawing
    if option == "a":
        print()

        turtle.speed(0)

        colors = ["turquoise","SteelBlue","RoyalBlue",
                  "purple","red","PaleGreen","OrangeRed",
                 "MediumPurple","DodgerBlue","DeepSkyBlue", "chocolate"]

        #drawing A:
        turtle.up()
        turtle.goto(-200,0)
        turtle.down()
        turtle.pencolor(random.choice(colors))
        turtle.left(80)
        turtle.forward(200)
        turtle.pencolor(random.choice(colors))
        turtle.right(150)
        turtle.forward(200)
        turtle.up()
        turtle.goto(-180,80)
        turtle.down()
        turtle.setheading(0)
        turtle.pencolor(random.choice(colors))
        turtle.forward(100)

        #Drawing B
        turtle.forward(5)
        turtle.circle(30,180)
        turtle.setheading(270)
        turtle.pencolor(random.choice(colors))
        turtle.forward(120)
        turtle.setheading(0)
        turtle.circle(30,180)

        

        """setheading() defines direction 0 means pointing right,
            90 points to north, 180 points to the left
            and 270 pointss straight down
                """

        #Drawing I
        turtle.up()
        turtle.goto(-15,15)
        turtle.down()
        turtle.setheading(90)
        turtle.pencolor(random.choice(colors))
        turtle.forward(120)

        #drawing D
        turtle.up()
        turtle.goto(20,15)
        turtle.color(random.choice(colors))
        for i in range(10):
            turtle.forward(12)
            turtle.dot(8)
        turtle.setheading(0)
        turtle.down()
        turtle.forward(40)
        turtle.up()
        turtle.color(random.choice(colors))
        angle=0
        turtle.setheading(180)
        while angle>-180:
            turtle.circle(55,-180/10)
            turtle.dot(8)
            angle=angle-18
        turtle.down()
        turtle.color(random.choice(colors))
        turtle.backward(40)
            
        
                    

turtle.done()
