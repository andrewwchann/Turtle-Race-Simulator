import turtle
import random
import time
width, height = 500, 500  # Constants
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black',
           'pink', 'brown', 'cyan']


def num_turtles():
    """Gets the amount of turtles for racing and checks if it
        is a valid input."""
    turtles = 0
    while True:
        turtles = input('Enter number of turtles (2-10): ')
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print('Invalid input, please try again!')
            continue

        # Only executes when the input is a number
        if turtles >= 2 and turtles <= 10:
            return turtles
        else:
            print('Input was not in range of 2-10, please try again!')


def turtle_screen():
    """Setting up the screen for the simulation. Put after the num_turtles so
        the screen will appear after a correct input."""
    screen = turtle.Screen()  # Creating the screen
    screen.setup(width, height)  # Makes the screen with the dimensions
    screen.title('Turtle Racing Simulator')

    # # Creating finish line
    # finish = turtle.Turtle()
    # finish.color('black')
    # finish.shape('arrow')
    # finish.speed(0)
    # finish.penup()
    # finish.setpos(-width//2, height//2 - 20)
    # finish.penup()
    # finish.forward(width)


def create_turtles(colours):
    """Creates the turtles on the screen and positions them at the bottom
        of the screen equally spaced."""
    turtles = []
    spacing = width // (len(colours) + 1)  # Creates optimal spacing
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()  # Saves instance
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)  # Rotates racers by 90 degrees
        racer.penup()
        racer.setpos(-width//2 + (i + 1) * spacing, -height//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colours):
    """Creates the race moving each turtle by a random number
        between 1-20 which controls the speed."""
    turtles = create_turtles(colours)

    while True:
        for racer in turtles:
            # Moves turtles from 1-20 pixels (dictates speed)
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()  # Gives us the x and y values (only need y)
            if y >= (height // 2 - 10):
                return colours[turtles.index(racer)]  # Return = break


racers = num_turtles()
turtle_screen()

random.shuffle(colours)  # Randomizing colours
turtle_colours = colours[:racers]  # Slicing list to the amount of racers

winner = race(turtle_colours)
turtle.write('The winner is:', winner, font=("Arial", 18, "normal"),
             align="center")
turtle.fillcolor(winner)
time.sleep(5)
