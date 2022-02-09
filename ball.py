import turtle
import math

class cherepaha():
    cherepaha = turtle.Turtle()
    cherepaha.shapesize(1)
    X = 0
    Y = 0

    def __init__(self, x, y):
        self.cherepaha.color('black')
        X_cor = self.cherepaha.xcor()
        Y_cor = self.cherepaha.ycor()
        self.cherepaha.penup()
        self.cherepaha.goto(x, y)

    def pos(self, x):
        self.X = x
        self.Y = math.sin(self.X)

    def dvig(self, u):
        self.cherepaha.goto(self.X, self.Y)
        u.update()
