import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.color("blue")
t=turtle.Screen()

colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
t.bgcolor(random.choice(colors))


rect = turtle.Turtle()
rect.speed(10)

for i in range(180):
    for colors in ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown", "grey", "cyan", "magenta"]:
        rect.color(colors)
        rect.forward(100)
        rect.right(30)
        rect.forward(20)
        rect.left(60)
        rect.forward(50)
        rect.right(30)
        rect.penup()
        rect.setposition(0, 0)
        rect.pendown()
        rect.right(2)
turtle.done()