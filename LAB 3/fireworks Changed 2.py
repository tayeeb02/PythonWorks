# fireworks
#turtle.setup(width, height) basically sets  up the width and height of the turtle window.
#turtle.bgpic("filename.extension") Adds a background image to an otherwise white image
#playsound.play("filename.extension")

#I COULDN"T ADD GRAVITATION EFFECT THE LAST TIME. FAILURE FROM MY PART

import random   # module providing the randint function
import time     # time module to delay after drawing five fireworks
import turtle   # turtle module for drawing fireworks
import playsound #if you want to play sound.

#### Initialize variables used in the program

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

#You can actually assign multiple values to multiple variables,
#In case of width and height, what it will do is assign 900 to width and 564 to height



#The reason we do this is to surround the program.

firework_radius = 100   # The maximum radius a firework can have
firework_count = 30     # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]
 

#### Initialize the turtle module

turtle.setup(screen_width, screen_height)   # Set the size of the screen
turtle.bgpic("hong_kong.gif")               # Put the background image on the
                                            # screen
turtle.width(3)                             # Draw lines with a width of three
turtle.shape("circle")                      # Set the turtle to be bomb shape
turtle.color("red")                         # Set the turtle color to red
turtle.speed(0)                            # Making turtle faster

"""
Turtle.shape is an interesting feature. It changes the shape of the turtle.

Why is it relevant to us? Because when we sent a bomb up for fireworks,
there is no way of creating a moving object. I mean there is but easiest way is to move the turtle itself.

Now, turtle by default has arrow shape which is not good if you're sending fireworks.


So, in this case, use shape to change the shape of the turtle.
Experiment with different shapes and see where it takes you and what it does. You must figure it out well.
"""
#bgpic is a feature to add background image.


#### For loop to shoot individual firework

for i in range(firework_count):
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1) #Wait 1 second before clearing.
        turtle.clear()

    #### Add your code here
    starty= -(screen_height/2)               # Firework starts from bottom of screen but random position
    #Note: Zero is dead center of the screen # Initialize a starting position
                                             # Initialize a destination
                                             # Shoot a firework from the start to the destination
    startx=random.randint(-int((screen_width/2)),int(screen_width/2)) #Any random position at the bottom of the screen
    #We needed to add int() function as the normal one will give float. Float does not work as argument for randint()

    #Going to the position

    turtle.up()
    turtle.hideturtle() #You arent' supposed to see the turtle when it moves back to origin
    
    turtle.goto(startx,starty)
    
    #Setting the firework's destination

    turtle.color("red")

    destx= random.randint(-int(screen_width/2),int(screen_width/2))
    desty=random.randint(0,int(screen_height/2)) #We want it to explode at the top half

    turtle.showturtle() #You want to see the turtle "bomb" go into sky.
    turtle.goto(destx,desty)
    turtle.down()
    

    
    #### The turtle is in the sky, explode the firework

    #### Add your code here
    # Pick a firework color from the firework colour list
    turtle.color(random.choice(firework_colours))


    # Pick a size for the firework
    radius=random.randint(firework_radius/2, firework_radius)
    radius_current =10

    
    # Pick the number of explosion directions
    directions= random.randint(10,30)

    #will increase each radius by 10 pixels

    
    #### For loop to draw each ring of explosion
    #This is the loop that draws the circle right
    for this_radius in range(10,radius,10): #Start 10, end at radius, step by 10 pixels

        #tracer function. it is responsible for handling the animations in turtle
        #We don't want to see the animation, only final product.
        #Tracer stops updating the screen
        turtle.tracer(False) #Remember, in True or False, first letter capital
        turtle.up()
        turtle.setheading(0) #point to right
        turtle.forward(this_radius)
        turtle.left(90)
        for i in range(directions):
            turtle.dot(this_radius/10) #Changes size of dot with each iteration
            turtle.circle(this_radius,360/directions)
        turtle.left(90)
        turtle.forward(this_radius)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        #playsound.play("explosion.wav") #This didn't work initially because I didn't download the audio
        #I only downloaded the LIBRARY
    turtle.hideturtle()
    turtle.tracer(True) #Resume updating the screen

    #### Add your code here


turtle.done() # Need to keep the window display up
#What if I remove this code at the end? What will happen then?

#It didn't do anything.
