# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

#Here I initialise a value to track my range
valueholder = 100
counter = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guesses
    if valueholder == 100:
        secret_number = random.randrange(0,100)
        guesses = int(math.ceil(math.log((100 - 0 + 1),2)))
        print ("New Game! The number is between 0 to 100!")
    elif valueholder == 1000:
        secret_number = random.randrange(0,1000)
        guesses = int(math.ceil(math.log((1000 - 0 + 1),2)))
        print ("New Game! The number is between 0 to 1000!")
    global counter
    counter = 0
    print ("You have " + str(guesses) + " guesses left!")
    print ("\n")

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game    
    global valueholder
    valueholder = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global valueholder
    valueholder = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    player_number = int(guess)
    print ("You guessed " + str(player_number) + "!")
    global counter 
    counter += 1
    guesses_left = guesses - counter
    if player_number == secret_number:
        print ("Correct!")
        new_game()
    elif guesses_left == 0:
        print ("Oops! You've lost! The secret number was " + str(secret_number)) + "!"
        new_game()
    else:
        if player_number < secret_number:
            print ("Higher!")
        else:
            print ("Lower!")
        if guesses_left > 1:
            print ("You have " + str(guesses_left) + " guesses left!")
        elif guesses_left == 1:
            print ("Your last guess! Make it count!")
        print ("\n")

# create frame
f = simplegui.create_frame("guessthenumber", 300, 300)
f.add_input("Guess!", input_guess, 100)
f.add_button("Play from 0 to 100!", range100)
f.add_button("Play from 0 to 1000!", range1000)

# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()
