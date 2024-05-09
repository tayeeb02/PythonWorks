# COMP1021 Robot Game Lab
# Name       : ABID, Mohammed Sirajul Mostafa
# Email      :msmabid@connect.ust.hk
# Student ID : 20914532

"""
This lab is crucial for you to learn about the state functions and shit. If you can't do this well, chances are, you can't do anything else well.
"""

# The following line imports the game function library and map into
#  this main program.
from game_lib import *
import time

# This is the only 'memory' of the robot that you can use to store things
#
# You are expected to use it to store only a string, which indicates the
#  current 'state' of the robot.
currentStateForTask1 = "Go north"
currentStateForTask2 = "Go north"
currentStateForTask3 = "Go north"
currentStateForTask4 = "Go north"

# These functions helps the robot to make the decision about what it needs
#  to do in order to get to the exit of the map.
# 
#  The function should return one of the following:
#     "NORTH"    which means the robot decides to go north
#     "SOUTH"    which means the robot decides to go south
#     "EAST"     which means the robot decides to go east
#     "WEST"     which means the robot decides to go west
#     "NONE"     which means the robot decides to stay in the same place

# Your task is to help the robot to make a decision on what to do next
#
#  A collection of functions that you will find very useful are shown here:
#
#    northIsWall()    returns True if the robot detects that the north side is blocked, otherwise it returns False
#    southIsWall()    returns True if the robot detects that the south side is blocked, otherwise it returns False
#    eastIsWall()     returns True if the robot detects that the east side is blocked, otherwise it returns False
#    westIsWall()     returns True if the robot detects that the west side is blocked, otherwise it returns False
#


# This is the function for task 0
def makeDecisionForTask0():
    return "NORTH"

# This is the function for task 1
def makeDecisionForTask1():
    global currentStateForTask1
    
    if currentStateForTask1 == "Go north":
        if northIsWall():
            currentStateForTask1 = "Go east"
            return "NONE" #Using none seems to be a better choice. Less Confusion
        else:
            return "NORTH"
    elif currentStateForTask1 == "Go east":
        if not northIsWall():
            currentStateForTask1 = "Go north"
            return "NONE"
        else:
            return "EAST"
        

# This is the function for task 2
def makeDecisionForTask2():
    global currentStateForTask2
    

    if currentStateForTask2 == "Go north":
        if northIsWall():
            currentStateForTask2 = "Go east"
            return "NONE" #Using none seems to be a better choice. Less Confusion
        else:
            return "NORTH"
    elif currentStateForTask2 == "Go east":
        if not northIsWall():
            currentStateForTask2 = "Go north"
            return "NONE"
        elif eastIsWall():
            currentStateForTask2 = "Go west"
            return "NONE"
        else:
            return "EAST"
    elif currentStateForTask2 == "Go west":
        if not northIsWall():
            currentStateForTask2= "Go north"
            return "NONE"
        else:
            return "WEST"
    

# This is the function for task 3
def makeDecisionForTask3():
    global currentStateForTask3

    if currentStateForTask3 == "Go north":
        if northIsWall():
            currentStateForTask3 = "Go east"
            return "NONE" #Using none seems to be a better choice. Less Confusion
        else:
            return "NORTH"
    elif currentStateForTask3 == "Go east":
        if not northIsWall():
            currentStateForTask3 = "Go north"
            return "NONE"
        elif eastIsWall():
            currentStateForTask3 = "Go west"
            return "NONE"
        else:
            return "EAST"
    elif currentStateForTask3 == "Go west":
        if not northIsWall():
            currentStateForTask3= "Go north"
            return "NONE"
        else:
            return "WEST"
 


# This is the function for task 4
def makeDecisionForTask4():
    global currentStateForTask4
    #time.sleep(1)

    #print(currentStateForTask4)

    
    if currentStateForTask4 == "Go north":
        if not eastIsWall():
            currentStateForTask4 = "Go east"
            return "EAST"
        elif northIsWall():
            currentStateForTask4 = "Go west"
            return "NONE"
        else:
            return "NORTH"
    elif currentStateForTask4 == "Go west":
        if not northIsWall():
            currentStateForTask4 = "Go north"
            return "NORTH"
        elif westIsWall():
            currentStateForTask4 = "Go south"
            return "NONE"
        else:
            return "WEST"
    elif currentStateForTask4 == "Go south":
        if not westIsWall():
            currentStateForTask4 = "Go west"
            return "WEST"
        elif southIsWall():
            currentStateForTask4= "Go east"
            return "NONE"
        else:
            return "SOUTH"
    elif currentStateForTask4 == "Go east":
        if not southIsWall():
            currentStateForTask4 = "Go south"
            return "SOUTH"
        elif eastIsWall():
            currentStateForTask4 = "Go north"
            return "NONE"
        else:
            return "EAST"

##stateForTask4 = "Find a wall first!"
##def makeDecisionForTask4():
##    global stateForTask4
##    if stateForTask4 == "Find a wall first!":
##        if leftIsWall():
##            stateForTask4 = "Go up"
##        else:
##            return "LEFT"
##    elif stateForTask4 == "Go up":
##        if leftIsWall():
##            stateForTask4 = "Go right"
##        else:
##            stateForTask4 = "Go left"
##            return "LEFT"
##    elif stateForTask4 == "Go down":
##        if rightIsWall():
##            stateForTask4 = "Go left"
##        else:
##            stateForTask4 = "Go right"
##            return "RIGHT"
##    elif stateForTask4 == "Go left":
##        if downIsWall():
##            stateForTask4 = "Go up"
##        else:
##            stateForTask4 = "Go down"
##            return "DOWN"
##    elif stateForTask4 == "Go right":
##        if upIsWall():
##            stateForTask4 = "Go down"
##        else:
##            stateForTask4 = "Go up"
##            return "UP"
##    return "NONE"
    
    

# The following line of code chooses the map of the game before it starts
# 
# You can change the map of the game by changing the parameters:
# 
# - Parameter 1 can be either:
#   - "task0", "task1", "task2", "task3" or "task4"
#     which mean the predefined maps from the task that you want to work on
#
#   - "custom"
#     which means any customized map(s) that you can add in game_map.py
#
# - Parameter 2 is a number representing the map you want to use
chooseGameMap("task4", 1)

#####
#
# !!! You DO NOT need to change anything from this point onwards !!!
#
#####

# Using the makeDecision function to set the Decision function used in each of the tasks
assignDecisionFuncForTask0(makeDecisionForTask0)
assignDecisionFuncForTask1(makeDecisionForTask1)
assignDecisionFuncForTask2(makeDecisionForTask2)
assignDecisionFuncForTask3(makeDecisionForTask3)
assignDecisionFuncForTask4(makeDecisionForTask4)

# Start the game
startGame()
