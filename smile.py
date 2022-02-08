import turtle
class Trey():
    def __init__(self):
        # треугольники посреди поля
        smile = turtle.Turtle()
        smile.hideturtle()
        smile.penup()
        smile.goto(0, 0)
        smile.pendown()
        smile.goto(100, 100)
        smile.goto(100, 0)
        smile.goto(100, 100)
        smile.penup()
        smile.goto(0, 0)
        smile.pendown()
        smile.goto(-100, 100)
        smile.goto(-100, 0)
        smile.goto(100, 0)
        smile.penup()
        smile.goto(0, 0)
        smile.pendown()
        smile.shape('circle')



