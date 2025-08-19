#
# TEXT-BASED RPG GAME
#

# --- 1. Game world Data ---
# Create a dictionary to hold all the game's locations (rooms)
# Each location should be its own dict with a description, exits, and items

print("this is where data will be stored")

# --- 2. Player classes ---
# Define player classes to manage the players attributes.
# These classes should keep track of the players name, current location, and inventory.

# --- 3. Game Fucntions ---
# a) Display Location Function
# Write a function that prints the description of the current room and a list of available exits and items.
#
# b) process Command Function
# this fucntion will take the player's input string and decide what to do
# it should check for keywords like 'go', 'look', 'get', 'inventory', etc.
#
# c) Main Game Loop
# this is the heart of the game. It runs continuously until the game ends.
# Insdie the loop:
#  - call the display location function to show the player hwere they are.
#  - get input from the player using the input() function.
#  - pass the input to the process command function.
#  - check for game-ending conditions (like winning or losing)

# --- 4. Start the Game ---
# create an instance of the player class and start the main game loop.
