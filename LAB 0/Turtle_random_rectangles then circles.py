import turtle
import random #This imports the random library allowing us to use random numbers.
import time #imports time module. helps create a time delay


turtle.tracer(False) #This is one of the most powerful tools. Note that tracer is spelt with lowercase letters nothing uppercase

#using tracer, you save a lot of display time because python doesn't waste time trying to display every individual part

#Python thinks about everything first and then does it altogether, saving time.altzone Almost instant
#For this one, I think it is better to use a loop, that way I won't have to define it every time.
#I'm thinking of a while loop, might be best.
#For the colors, all the rectangles shall be black.


#This program will allow you to draw 50 random rectangle drawings


#Here, we will first draw 10 random, colored rectangles and then 10 random colored circles.

"""
Ok. Basically this function is supposed to give me both rectangles and circles. First it draws 20 rectangles and then delays for 4 seconds and then draws
20 circles. But when I use a tracer, it will skip displaying the rectangles part. It will only display the circles. However, it is because tracer(False) is at the very beginning and tracer(True)
is at the very end. I can break it in the middle by closing tracer shit in the middle.

"""

colors = ["Royal Blue", "Pale Green", "Gold", "Rosy Brown", "Coral", "Orchid",
          "white smoke", "dodger blue", "deep sky blue", "medium slate blue"]

turtle.width(5)

count=0
turtle.speed(0)

while count<20:   #Allows you to draw 20 random rectangles. count<20 means 20. count<=20 means 21 values because it starts from 0.
    turtle.up() #prevents drawing
    random_x= random.randint(-300,300) #sets position
    random_y= random.randint(-300,300) #sets position
    random_angle=random.randint(0,360)  #sets initial angle
    random_width= random.randint(50,100) #sets width
    random_height= random.randint(30,120) #sets height

    turtle.goto(random_x,random_y) #goes to the said position
    turtle.down() #allows turtle do draw
    turtle.left(random_angle)

    turtle.pencolor(random.choice(colors)) #random.choice() This is how you choose without using an index. 
    turtle.fillcolor(random.choice(colors))

    turtle.begin_fill()
    
    turtle.forward(random_width)
    turtle.left(90)
    turtle.forward(random_height)
    turtle.left(90)
    turtle.forward(random_width)
    turtle.left(90)
    turtle.forward(random_height)

    turtle.end_fill()

    #The problem here, I set up a count condition, yes but I didn't increase the count. That's why it was going indefinitely.

    count=count+1 #increases count so that the condition can end eventually.

turtle.hideturtle() #hides the turtle

turtle.tracer(True) 
#Ok. There seems to be a problem here. That is, it executes the code well, no problem there, but it immediately clears the rectangle and goes to circles.
#There is absolutely no time for you to admire the painting.

##count_T=0
##while count_T<=100: #Hopefully this adds a time delay.
##    count_J=0
##    while count_J<=1000000: #This adds sufficient delay 
##        count_J=count_J+1
##    count_T=count_T+1

"""
The previous ## commented out region was what code I used at the beginning of semester when I didn't use time modules. Now I'm good at it.


"""
time.sleep(10) #This basically adds a time delay of 10 seconds.


turtle.clear() #This clears the turtle window so that the new ones don't overlap
turtle.showturtle() #shows the turtle
count=0 #Just for safety, I don't know the last value of count.

turtle.tracer(False)

while count<20:
    turtle.up()
    random_x=random.randint(-300,300)
    random_y=random.randint(-300,300)
    random_radius= random.randint(30,150)

    turtle.pencolor(random.choice(colors)) #This sets up a random pencolor from a set of options

    turtle.fillcolor(random.choice(colors))

    turtle.goto(random_x, random_y)
    turtle.down()

    turtle.begin_fill() #this code allows you to fill in a closed shape.

    turtle.circle(random_radius)

    turtle.end_fill() #This code is needed to end the fill shape.

    count=count+1


turtle.hideturtle()
#turtle.tracer(True)

turtle.done()

"""
Won't use tracer here because this code relies on having separate drawing. But I will try.

Tracer should technically just give the final product, circles. 
"""
