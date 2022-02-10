import turtle # библиотека

class Trey(): # новый класс
    def __init__(self): # конструктор класса
        smile = turtle.Turtle() # новый объект
        smile.hideturtle() # спрятать черепаху
        smile.penup() # поднял карандаш
        smile.goto(0, 280) # перемещение
        smile.pendown() # опустил карандаш
        for i in range(360): # цикл
            smile.right(1) # поворот
            smile.forward(2) # перемещение
        smile.penup() # поднял карандаш
        smile.goto(40, 120) # перемещение
        smile.left(180) # поворот
        smile.pendown() # опустил карандаш
        smile.forward(80) # перемещение
        smile.penup() # поднял карандаш
        smile.goto(-40, 250) # перемещение
        smile.left(90) # перемещение
        smile.pendown() # опустил карандаш
        smile.forward(50) # перемещение
        smile.penup() # поднял карандаш
        smile.goto(40, 250) # перемещение
        smile.pendown() # опустил карандаш
        smile.forward(50) # перемещение

    def lose(self, x, y, z, m, u, i, o, p): # новый метод
        smil = turtle.Turtle() # новый объект
        smil.penup() # поднял карандаш
        smil.color("red") # цвет красный
        smil.goto(m, i) # перемещение
        smil.right(o) # поворот
        smil.pendown() # опустил карандаш
        smil.forward(i) # перемещение
        smil.penup() # поднял карандаш
        smil.goto(m, i) # перемещение
        smil2 = turtle.Turtle() # новый объект
        smil2.color("black") # цвет черный
        smil2.penup() # поднял карандаш
        smil2.goto(z, p) # перемещение
        smil2.left(u) # поворот
        smil2.pendown() # опустил карандаш
        for i in range(o): # цикл
            smil2.forward(x) # перемещение
            smil2.left(x) # поворот
