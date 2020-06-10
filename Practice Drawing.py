# Written by Gabe Mohs
# gabemohs12@gmail.com

import turtle
my_turtle = turtle.Turtle()

my_turtle.speed(1000000000)
distance = 100

for n in range(6):
    for n in range(100):
        for n in range(3):
            my_turtle.forward(distance)
            my_turtle.right(120)
        my_turtle.right(3.6)
    distance *= 1.5

turtle.done()