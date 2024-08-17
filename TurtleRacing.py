"""
Races a number of turtles based on user input.
"""

from turtle import *
from time import *
from random import *

WIDTH = 600
HEIGHT = 600

def get_turtles():
    """
    Gets how many turtles the user wants to race.
    """
    while True:
        try:
            turtles_num = int(input("How many turtles would you like to race? "))
            return turtles_num
        except ValueError:
            print("Only integers are accepted. Try again.")

def make_screen():
    """
    Initiates the drawing screen.
    """
    screen = Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Race the turtles!")
    screen.colormode(255)

def make_turtles(turtles_num):
    """
    Makes turtles_num turtles and returns a list of all the turtle objects.
    """
    all_turtles = []
    spacing = WIDTH/(turtles_num + 1)
    for num in range(turtles_num):
        t = Turtle()
        t.color(randint(0,255),randint(0,255),randint(0,255))
        t.shape("turtle")
        t.left(90)
        t.pu()
        t.goto(spacing * (num + 1) - (WIDTH/2), -HEIGHT/2 + 20)
        t.pd()
        all_turtles.append(t)

    return all_turtles

def race(all_turtles):
    """
    Races all turtle objects in a given list.
    """
    while True:
        for turtle in all_turtles:
            turtle.fd(randint(0,20))
            x,y = turtle.pos()
            if y >= HEIGHT / 2 - 10:
                return turtle.color()[0]


def main():
    """
    Starts the program
    """
    turtles_num = get_turtles()
    make_screen()
    all_turtles = make_turtles(turtles_num)
    color = race(all_turtles)
    print(f"The turtle with RGB code of {color} won!!")

#initiates program
main()
sleep(5)