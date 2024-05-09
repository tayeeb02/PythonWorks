# COMP1021 Music System
#Done by: ABID, Mohammed Sirajul Mostafa SID: 20914532

import turtle # Import the turtle module for drawing
import music  # Import the music module for playing music
import time   # Import the time module for time.sleep()

# Initialize the music data
music_data = []

# Store the current instrument
instrument = 0

# A dictionary containing the menu settings
main_menu = {
    # menu key: (caption, position and size, colour)
    "load" : ("Load Music", (-250, 20, 220, 140), "cyan"),
    "play" : ("Play Music", (0, 20, 220, 140), "yellow"),
    "instrument" : ("Change Instrument", (250, 20, 220, 140), "magenta"),
    "transpose" : ("Transpose Music", (-250, -150, 220, 140), "orange"),
    "speed" : ("Adjust Speed", (0, -150, 220, 140), "red"),
    "crazymusic" : ("Make Crazy Music", (250, -150, 220, 140), "lawn green")
}


# This function draws a coloured box at (x, y) with a size of (w, h)
def drawBox(color, x, y, w, h):
    turtle.fillcolor(color)
    turtle.goto(x - w / 2, y - h / 2)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x, y)

    
# This function creates the menu on the turtle window
def drawMenu():
    turtle.hideturtle()
    turtle.up()
    turtle.width(5)

    turtle.tracer(False)    # Disable any turtle animation
    
    turtle.clear()

    # Write the title
    turtle.goto(0, 200)
    turtle.write("♪ Python Music System ♪", align="center", \
                 font=("Arial", 30, "bold"))

    # Draw the menu boxes
    for menu_info in main_menu.values():
        caption = menu_info[0]
        x, y, w, h = menu_info[1]
        color = menu_info[2]

        drawBox(color, x, y, w, h)

        turtle.goto(x, y - 10)
        turtle.write(caption, align="center", \
                     font=("Arial", 16, "bold"))

    turtle.tracer(True)    # Refresh the turtle window


# This function shows the music summary
def updateMusicSummary():

    global instrument
    
    text_turtle.up()
    text_turtle.hideturtle()

    text_turtle.clear()
    text_turtle.goto(0, 140)

    if len(music_data) == 0:
        # Music is empty
        summary = "Click on the 'Load Music' area to load a music file"
    else:
        # Number of notes
        summary = "No. of notes = " + str(len(music_data)) + ", "


        # Duration
        duration = 0
        for note in music_data:
            if note[0] + note[2] > duration:
                duration = note[0] + note[2]
        mins = int(duration / 60)
        secs = round(duration % 60, 2)
        summary = summary + "song duration = " + str(mins) + "m " + str(secs) + "s"

        #####
        #
        # TODO:
        # - Update and display the instrument appropriately
        #
        #####
        current_instrument= music.instrument_list[instrument]

        summary= summary +", instrument = "+ current_instrument

        
        
        
    text_turtle.write(summary, align="center", font=("Arial", 14, "normal"))


# This function loads some music into the music data list
def loadMusic():
    global music_data
    

    # Get the song list from the song folder
    song_list = music.getsonglist()
    song_menu = ""
    for i in range(len(song_list)):
        song_menu = song_menu + str(i) + ": " + song_list[i][0] + "\n"
    if song_menu == "":
        song_menu = "No music files available"
    
    # Ask the user for the music file
    filename = turtle.textinput("Music File", song_menu + \
                   "\nPlease give me a music file number or a file name:")
    if filename == None:
        return

    # Get the song for numeric input
    if filename == None:
        return
    else: 
        if filename.isnumeric() and int(filename)>=0 and int(filename)<=len(song_list):
            filename = song_list[int(filename)][1]
        elif int(filename) <=0:
            filename= song_list[0][1]
        else:
            filename = song_list[len(song_list)-1][1]

    # Open the file for reading
    file = open(filename, "r")

    # Reset the music data
    music_data = []

    # Read the data into the music list
    for line in file:
        # Read each line as a music note
        note = line.rstrip().split("\t")

        # Convert the data to the right data type
        note[0] = float(note[0])  # Time
        note[1] = int(note[1])    # Pitch
        note[2] = float(note[2])  # Duration

        # Add the note at the end of the music
        music_data.append(note)

    # Close the file
    file.close()

    # Update the music summary
    updateMusicSummary()


# This function plays the music
def playMusic():
    global music_data

    # Clear the music data in the music module
    music.clear()

    # Add the music notes
    for i in range(len(music_data)):
        # Show progress every 10 notes, ie, only update the value shown on screen every 10 notes.
        if i % 10 == 0: #without this, the display updates every single note. tried with i%1==0. 
            turtle.tracer(False) #NOTE: turtle.tracer() basically prevents flashing of text that shows how many notes were loaded
            text_turtle.clear()
            text_turtle.write("Adding note " + str(i) + \
                              " of " + str(len(music_data)), \
                              align="center", font=("Arial", 14, "normal"))
            turtle.tracer(True)

        # Add the note
        note = music_data[i]
        music.addnote(note[0], note[1], note[2])

    # Update the music summary
    updateMusicSummary()

    # Play the music
    music.play()


# This function changes the instrument
def changeInstrument():
    global instrument

    #####
    #
    # TODO:
    # - Change the instrument appropriately
    # - Show the instrument list in the input box
    # - Update the instrument display
    #
    #####
    info_for_instr = "" #Remember the multiple line string method. It works.
    list_of_instruments= [0,10,19,24,32,40,56,64,73,123]

    for instrument in list_of_instruments:
        info_for_instr = info_for_instr + \
                         str(instrument) + ": " + music.instrument_list[instrument] + "\n"
    #print(info_for_instr)
    
    display_information= info_for_instr + "\n" + "Please enter the instrument number (0-127):"
    #Newline character must be enclosed in quotation marks. \n was used here to put another line between
    #the instrument list and the instrument number
    

    instru_selected= turtle.numinput("Change Instrument", display_information)
    #Note: in numinput or textinput, the third part after comma is the place holder.
    if instru_selected == None:
        return
    else:
        instru_selected= int(max(0,min(instru_selected,127)))

    if instru_selected> 127 or instru_selected<0:
        return


    #print(instru_selected)

    music.setinstrument(instru_selected) #sets the instrument

    instrument= instru_selected

    


# This function transposes the music pitch
def transpose():
    global music_data
    
    #####
    #
    # TODO:
    # - Ask for the transposition number
    # - Adjust the pitch of all notes appropriately
    #
    #####
    change = turtle.numinput("Transpose", "Please enter the transposition: ")
    #print(str(type(change)))
    
    if change == None:
        return
    else:
        change = int(change)

    for i in range(len(music_data)):
        music_data[i][1]= max(0, min( 127, music_data[i][1] + change))
        #print(music_data[i][1]) Worked like a charm
        



# This function adjusts the speed of the music
def adjustSpeed():
    global music_data

    #####
    #
    # TODO:
    # - Ask for the speed change percentage
    # - Adjust the speed of all notes appropriately
    # - Update the music summary
    #
    #####
    tr_value= turtle.numinput("Adjust Speed", "Please enter speed percentage: ")

    if tr_value == None :
        return
    else:
        tr_value = float(tr_value/100)

    for i in range(len(music_data)):
        if tr_value== 0:
            music_data[i][0]= 0
            music_data[i][2]=0
        else:
            music_data[i][0]= float(music_data[i][0]/tr_value)
            music_data[i][2]= float(music_data[i][2]/tr_value)

    updateMusicSummary()

# This function makes a piece of crazy music in the music list

def makeCrazyMusic():
    global music_data
    number_of_sequence = turtle.numinput("Crazy Music","Enter the number of times to play the music sequence: ")
    if number_of_sequence == None:
        return
    number_of_sequence = int(number_of_sequence)
    duration = turtle.numinput("Crazy Music","Enter the duration of each music sequence: ")
    if duration == None:
        return
    duration = float(duration)
    starting_pitch = turtle.numinput("Crazy Music","Enter the starting pitch of the music sequence: ")
    if starting_pitch == None:
        return
    starting_pitch = int(starting_pitch)
    ending_pitch = turtle.numinput("Crazy Music","Enter the ending pitch of the music sequence: ")
    if ending_pitch == None:
        return
    ending_pitch = int(ending_pitch)
    number_of_pitch = 0
    if(starting_pitch < ending_pitch):
        number_of_pitch = ending_pitch - starting_pitch + 1
    else:
        number_of_pitch = starting_pitch - ending_pitch + 1

    music_data = []
    
    notee = []
    a = 0
    a = float(a)
    notee.append(a)
    b = 0
    b = int(b)
    notee.append(b)
    notee.append(a)
    count=0
    if(starting_pitch < ending_pitch):
        for index in range(0, number_of_sequence):
            for pitch in range(starting_pitch, ending_pitch+1):
                notee[0] += count * (duration/number_of_pitch)
                notee[1] = pitch
                notee[2] = float(duration/number_of_pitch)
                
                music_data.append(notee)
                notee=[0,0,0]
                count= count +1
                print(music_data)
    else:
        for index in range(0, number_of_sequence):
            for pitch in range(starting_pitch, ending_pitch-1, -1):
                notee[0] += notee[2]
                notee[1] = pitch
                notee[2] = float(duration/number_of_pitch)
                music_data.append(notee)
                notee=[0,0,0]
                count = count +1

    print(music_data)
    updateMusicSummary()

# This function handles the screen click and the menu selection
def handleMenu(x, y):
    # Get the menu item that the user has clicked on
    selected_key = None
    for key, menu_info in main_menu.items():
        menux, menuy, menuw, menuh = menu_info[1]
        if x > menux - menuw / 2 and x < menux + menuw / 2 and \
           y > menuy - menuh / 2 and y < menuy + menuh / 2:
            selected_key = key

    # Run the corresponding functions for each menu item
    if selected_key == "load":
        loadMusic()
    elif selected_key == "play":
        playMusic()
    elif selected_key == "instrument":
        changeInstrument()
    elif selected_key == "transpose":
        transpose()
    elif selected_key == "speed":
        adjustSpeed()
    elif selected_key == "crazymusic":
        makeCrazyMusic()
        

# Set up the turtle module
turtle.setup(800, 600)
turtle.speed(0)

# Show the menu
drawMenu()

# Create a new turtle to show music summary
text_turtle = turtle.Turtle()

# Update the music summary
updateMusicSummary()

# Set up the screen click event
turtle.onscreenclick(handleMenu)

turtle.done()

# Kill any currently playing sounds and remove the sound
music.stop(True)
