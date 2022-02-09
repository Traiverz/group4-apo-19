import turtle
import math

class cherepaha():
    cherepaha = turtle.Turtle()
    X = 0
    Y = 0
    def __init__(self):
        self.cherepaha.color('black')  # задаем ей зелёный цвет
        X_cor = self.cherepaha.xcor()  # новая переменная, содержащая координату Х нашей черепашки
        Y_cor = self.cherepaha.ycor()  # новая переменная, содержащая координату У нашей черепашки
        self.cherepaha.penup()  # поднимаем карандаш отрисовки
        self.cherepaha.goto(-300, 0)

    def pos(self, x):
        if self.X > - 300:
            self.X = x  # координата Х черепахи берёт значение переменной из начала программы
            self.Y = math.sin(self.X)  # координата У высчитывается по математической формуле
        else:
            self.X = -x  # координата Х черепахи берёт значение переменной из начала программы
            self.Y = math.sin(self.X)  # координата У высчитывается по математической формуле
        if self.X > 300:
            self.X = self.X * -1


    def dvig(self, u):
        self.cherepaha.goto(self.X, self.Y)
        u.update()
        #print(self.X, self.Y)
