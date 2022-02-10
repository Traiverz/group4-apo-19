import turtle # библиотека черепахи
import math # библиотека математическая

class cherepaha(): # создал класс
    cherepaha = turtle.Turtle() # задал переменную класса
    cherepaha.shapesize(1) # задал размер переменной
    X = 0 # переменная
    Y = 0 # переменная

    def __init__(self, x, y): # конструктор класса
        self.cherepaha.color('black') # передаем цвет объекта
        X_cor = self.cherepaha.xcor() # новая переменная координаты
        Y_cor = self.cherepaha.ycor() # новая переменная координаты
        self.cherepaha.penup() # поднял карандаш
        self.cherepaha.goto(x, y) # перемещение переменной

    def pos(self, x): # метод позиции
        self.X = x # новая координата х
        self.Y = math.sin(self.X) # новая координата у

    def dvig(self, x): # метод движения
        self.cherepaha.goto(self.X, self.Y) # перемещаем координаты
        x.update() # обновляем переменную
