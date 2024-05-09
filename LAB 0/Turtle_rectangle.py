#This is a program to draw a rectangle.

import turtle #importing turtle module

#Note turtle always starts by facing the right. It will always do that.
#When you use go to command, it will only shift to that position, but its orientation will remain the same

turtle.width(5) #Setting the width of the turtle.
turtle.color("blue") #This sets the color of the pen
turtle.penup() #this prevents turtle from drawing anything when going to that position, otherwise it will draw

turtle.goto(-100,50)
turtle.pendown() #allows turtle to start drawing again.

turtle.forward(200) #the turtle moves forward ie in the direction of the orientation(right in this case)
#turtle is now at (100,50)
turtle.right(90) #Turtle turns 90 degrees to the right, ie downwards.
turtle.forward(100) #Moves 100 pixels forward ie, 100 pixels down in this case
turtle.right(90) #turns 90 degrees to the right again
turtle.forward(200) #moves 200 steps forward
turtle.right(90) #again a 90 degree turn
turtle.forward(100) #Moves forward

#The core works in this form.
#Lets try adding space after the dot. See what happens.
# Adding space after dot ie turtle.  forward(100) does nothing, it executes the code in the same way anyway. 


#This is one way to do it. You can spam go to function repeatedly. Shortening the code as follows.

turtle.clear() #This clears the screen
#After clearing hte screen, turle remains in the last place where it was. You want it to go to the origin

turtle.penup()
turtle.goto(0,0) #this returns us to the origin. Now we have a blank slate.

#Redoing the code but differently this time.

#Remember the pen has still not been lowered at this stage.

turtle.goto(-100,50)
turtle.pendown() #Now the turtle can start drawing)

turtle.goto(100,50)
turtle.goto(100,-50)
turtle.goto(-100,-50)
turtle.goto(-100,50)

#The above code should give us a rectangle if everything is right. Lets execute.
#This code works much much better than before. It is much easier to go to specific locations on a straight line rather than specifying the length and angle
#It still depends on the code that you're given tho.

#Note for penup and pendown, you can simplify it as turtle.up() and turtle.down()


#go to function is absolute, goes to a specific position regardless of your start.

#forward is relative. It moves a certain distance and rotates a certain angle relative to your starting position. Remember this. 

turtle.done() #finishing the code #Just like HTML
