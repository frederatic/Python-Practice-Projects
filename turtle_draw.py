import turtle

def draw_square(turtle_name):
    for i in range(1,5):
        turtle_name.forward(100)
        turtle_name.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    fred = turtle.Turtle()
    fred.shape("turtle")
    fred.color("yellow")
    for i in range(1,37):
        draw_square(fred)
        fred.right(10)
    bob = turtle.Turtle()
    bob.shape("arrow")
    bob.color("white")
    bob.circle(100)
    window.exitonclick()

draw_art()
