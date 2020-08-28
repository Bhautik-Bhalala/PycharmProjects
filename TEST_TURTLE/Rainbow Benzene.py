# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['violet','indigo', 'blue', 'green', 'yellow', 'orange', 'red']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(0)


for x in range(360):
    t.pencolor(colors[x%7])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(50)