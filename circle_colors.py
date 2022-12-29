import turtle    # import turtle module
import random    # import random module

t = turtle.Turtle()   # create a turtle object
t.speed(0)
t.color("blue")      
t=turtle.Screen()     # create a screen object

colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
t.bgcolor(random.choice(colors))         # set the background color


rect = turtle.Turtle()
rect.speed(10)

for i in range(180):     # for loop for the circle
    for colors in ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown", "grey", "cyan", "magenta"]:
        rect.color(colors)      # set the color of the circle
        rect.forward(100)       # move the turtle forward
        rect.right(30)
        rect.forward(20)
        rect.left(60)
        rect.forward(50)
        rect.right(30)
        rect.penup()
        rect.setposition(0, 0)    # set the position of the turtle
        rect.pendown()            # draw a line
        rect.right(2)
turtle.done()                     # turtle done
