import turtle
import random #This imports the random library allowing us to use random numbers.

#For this one, I think it is better to use a loop, that way I won't have to define it every time.
#I'm thinking of a while loop, might be best.
#For the colors, all the rectangles shall be black.

turtle.tracer(False) #Stops displaying animation 
#This program will allow you to draw 50 random rectangle drawings

turtle.pencolor("royalblue")
turtle.fillcolor("cornflowerblue")
turtle.width(5)

count=0

while count<=20:   #Allows you to draw 21 random rectangles. because it goes from 0 to 20 inclusive so 21 values
    turtle.up() #prevents drawing
    random_x= random.randint(-300,300) #sets position
    random_y= random.randint(-300,300) #sets position
    random_angle=random.randint(0,360)  #sets initial angle
    random_width= random.randint(50,100) #sets width
    random_height= random.randint(30,120) #sets height

    turtle.goto(random_x,random_y) #goes to the said position
    turtle.down() #allows turtle do draw
    turtle.left(random_angle)

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

turtle.hideturtle()

turtle.tracer(True) #Displays the final result of whatever animation that went on before this line. This makes the program super fast.
#Almost instantaneous. #YES. The result was instantaneous. Literally, the moment I clicked F5, it worked. 
turtle.done()
