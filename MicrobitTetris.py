{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # This was created for my Digital Tech assigment and you can use this, alter the code or just learn\
# This took me 10+ hours to work on and make since im not that good with python on microbits\
# If you use this for anything give me some credits :)\
\
# Imports for the microbit\
from microbit import *  # Import microbit library for hardware control\
from random import choice  # Import choice function to randomly select bricks\
import music  # Import music library for playing sounds\
\
# Tetris grid setup\
grid=[[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]  # Create 6x7 grid with borders\
bricks = [[9,9],[9,0]],[[9,9],[0,9]],[[9,9],[9,9]],[[9,9],[0,0]]  # Define different brick shapes\
# Selects a block to place\
brick = choice(bricks)  # Randomly choose a brick from available shapes\
x=3  # Set initial x position for brick\
y=0  # Set initial y position for brick\
frameCount=10  # Initialize frame counter for game timing\
\
# Sounds for the game\
music.play(["C4:4","E4:4","G4:4","C5:8"], wait=False)  # Play startup melody\
\
# Paramaters for brightness \
def brightness (value):  # Define function to clamp brightness values\
    if value<0:  # If value is less than 0\
        return 0  # Return 0 (minimum brightness)\
    elif value>9:  # If value is greater than 9\
        return 9  # Return 9 (maximum brightness)\
    else:  # If value is between 0 and 9\
        return value  # Return the original value\
    # Small control function for computer to interpret \
def max(a,b):  # Define custom max function\
    if a>=b:  # If a is greater than or equal to b\
       return a  # Return a\
    else:  # If b is greater than a\
        return b  # Return b\
# Brick Stuff\
def hideBrick():  # Define function to hide current brick from display\
    if x>0:  # If brick is not at left edge\
        display.set_pixel(x-1,y,grid[y][x])  # Restore grid pixel at brick position\
    if x<5:  # If brick is not at right edge\
        display.set_pixel(x+1-1,y,grid[y][x+1])  # Restore grid pixel at brick position\
    if x>0 and y<4:  # If brick is not at edges\
        display.set_pixel(x-1,y+1,grid[y+1][x])  # Restore grid pixel at brick position\
    if x<5 and y<4:  # If brick is not at edges\
        display.set_pixel(x+1-1,y+1,grid[y+1][x+1])  # Restore grid pixel at brick position\
 # More brick stuff \
def showBrick():  # Define function to display current brick\
    if x>0:  # If brick is not at left edge\
        display.set_pixel(x-1,y,max(brick[0][0],grid[y][x]))  # Show brick pixel or grid pixel (whichever is brighter)\
    if x<5:  # If brick is not at right edge\
        display.set_pixel(x+1-1,y,max(brick[0][1],grid[y][x+1]))  # Show brick pixel or grid pixel (whichever is brighter)\
    if x>0 and y<4:  # If brick is not at edges\
        display.set_pixel(x-1,y+1,max(brick[1][0],grid[y+1][x]))  # Show brick pixel or grid pixel (whichever is brighter)\
    if x<5 and y<4:  # If brick is not at edges\
       display.set_pixel(x+1-1,y+1,max(brick[1][1],grid[y+1][x+1]))  # Show brick pixel or grid pixel (whichever is brighter)\
 # Rotating fucntion for brick\
def rotateBrick():  # Define function to rotate current brick\
    pixel00 = brick[0][0]  # Store top-left pixel value\
    pixel01 = brick[0][1]  # Store top-right pixel value\
    pixel10 = brick[1][0]  # Store bottom-left pixel value\
    pixel11 = brick[1][1]  # Store bottom-right pixel value\
    if not ((grid[y][x]>0 and pixel00>0) or (grid[y+1][x]>0 and pixel10>0) or (grid[y][x+1]>0 and pixel01>0) or (grid[y+1][x+1]>0 and pixel11>0)):  # Check if rotation is possible without collision\
        hideBrick()  # Hide current brick position\
        brick[0][0] = pixel10  # Rotate pixels clockwise\
        brick[1][0] = pixel11  # Rotate pixels clockwise\
        brick[1][1] = pixel01  # Rotate pixels clockwise\
        brick[0][1] = pixel00  # Rotate pixels clockwise\
        showBrick()  # Show brick at new orientation\
 # Fucntion for when the brick moves\
def moveBrick(delta_x,delta_y):  # Define function to move brick by given delta\
    global x,y  # Access global x and y variables\
    move=False  # Initialize move flag as false\
    if delta_x==-1 and x>0:  # If moving left and not at left edge\
        if not ((grid[y][x-1]>0 and brick[0][0]>0) or (grid[y][x+1-1]>0 and brick[0][1]>0) or (grid[y+1][x-1]>0 and brick[1][0]>0) or (grid[y+1][x+1-1]>0 and brick[1][1]>0)):  # Check if movement is possible\
            move=True  # Set move flag to true\
    elif delta_x==1 and x<5:  # If moving right and not at right edge\
        if not ((grid[y][x+1]>0 and brick[0][0]>0) or (grid[y][x+1+1]>0 and brick[0][1]>0) or (grid[y+1][x+1]>0 and brick[1][0]>0) or (grid[y+1][x+1+1]>0 and brick[1][1]>0)):  # Check if movement is possible\
            move=True  # Set move flag to true\
    elif delta_y==1 and y<4:  # If moving down and not at bottom\
        if not ((grid[y+1][x]>0 and brick[0][0]>0) or (grid[y+1][x+1]>0 and brick[0][1]>0) or (grid[y+1+1][x]>0 and brick[1][0]>0) or (grid[y+1+1][x+1]>0 and brick[1][1]>0)):  # Check if movement is possible\
            move=True  # Set move flag to true\
    if move:  # If movement is possible\
        hideBrick()  # Hide brick at current position\
        x+=delta_x  # Update x position\
        y+=delta_y  # Update y position\
        showBrick()  # Show brick at new position\
    return move  # Return whether movement occurred\
# Function for the game to check if the line is broken and if so then you get point\
def checkLines():  # Define function to check for completed lines\
    global score  # Access global score variable\
    removeLine=False  # Initialize remove line flag as false\
    for i in range(0, 5):  # Loop through each row (excluding borders)\
        if (grid[i][1]+grid[i][2]+grid[i][3]+grid[i][4]+grid[i][5])==45:  # Check if row is full (sum of brightness values = 45)\
            removeLine = True  # Set remove line flag to true\
            score+=10  # Add 10 points to score\
            for j in range(i,0,-1):  # Loop from current row to top\
                grid[j] = grid[j-1]  # Move each row down\
            grid[0]=[1,0,0,0,0,0,1]  # Reset top row to empty\
    if removeLine:  # If lines were removed\
        for i in range(0, 5):  # Loop through display columns\
            for j in range(0, 5):  # Loop through display rows\
                display.set_pixel(i,j,grid[j][i+1])  # Update display with new grid\
    return removeLine  # Return whether lines were removed\
\
gameOn=True  # Initialize game state as active\
score=0  # Initialize score to 0\
showBrick()  # Display initial brick\
# Functions while the game is running\
while gameOn:  # Main game loop\
    sleep(100)  # Pause for 100ms\
    frameCount+=1  # Increment frame counter\
    if button_a.is_pressed() and button_b.is_pressed():  # If both buttons pressed\
        rotateBrick()  # Rotate current brick\
    elif button_a.is_pressed():  # If only button A pressed\
        moveBrick(-1,0)  # Move brick left\
    elif button_b.is_pressed():  # If only button B pressed\
        moveBrick(1,0)  # Move brick right\
 \
    if frameCount==15 and moveBrick(0,1) == False:  # If time to move down and can't move down\
        frameCount=0  # Reset frame counter\
        grid[y][x]=max(brick[0][0],grid[y][x])  # Merge brick with grid\
        grid[y][x+1]=max(brick[0][1],grid[y][x+1])  # Merge brick with grid\
        grid[y+1][x]=max(brick[1][0],grid[y+1][x])  # Merge brick with grid\
        grid[y+1][x+1]=max(brick[1][1],grid[y+1][x+1])  # Merge brick with grid\
 \
        if checkLines()==False and y==0:  # If no lines cleared and brick at top\
            gameOn=False  # End game\
            # Better game over sound\
            music.play(["G3:4","E3:4","C3:8"], wait=True)  # Play game over melody\
        else:  # If game continues\
            x=3  # Reset brick x position\
            y=0  # Reset brick y position\
            brick = choice(bricks)  # Select new random brick\
            showBrick()  # Display new brick\
 \
    if frameCount==15:  # If time to move down\
       frameCount=0  # Reset frame counter\
# Sleep when you die and game score display at end\
sleep(2000)  # Pause for 2 seconds after game ends\
display.scroll("Score: " + str(score))  # Display final score}