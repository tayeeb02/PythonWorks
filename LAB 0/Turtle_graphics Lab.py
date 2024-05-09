import turtle #Turtle is a separate package so you'll need to import it to run it in shell

turtle.write("Hello World!") #turtle is going to write hello world.

text = """\
This is a multi-line string. I learnt about it in the lab 6. \

Thought it might be useful here

I can type on this line.

I can also type on this line.

"""

turtle.write(text)

turtle.done()#This command tells idle to stop executing the turtle module.

#Anything after turtle.done() will not be executed under the turtle module. It will simply not draw it.  

#turtle.circle(100) #Made this part as comment so it doesn't interfere with any code later.

#Turtle.write basically displays any text on a GUI window. Otherwise, it won't show on screen.

"""
using print shows it in IDLE window, using write shows it on turtle window.

You can use many lines using triple brackets.

Triple brackets that are not attached to any variable are considered multi line comments.

But triple brackets that are assigned to a variable means that you're using a multi-line string

"""

