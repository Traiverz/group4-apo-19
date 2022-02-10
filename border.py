import turtle # библиотека туртл

class Border(): # создал класс
    def __init__(self, x, y): # конструктор класса
        border = turtle.Turtle() # создал объект внешнего класса туртл
        border.hideturtle() # спрятал черепашку
        border.penup() # поднял карандаш
        border.goto(-x, y) # перемещаем на заданную координату
        border.pendown() # опустил карандаш
        border.goto(x, y) # перемещение
        border.goto(x, -y) # перемещение
        border.goto(-x, -y) # перемещение
        border.goto(-x, y) # перемещение
        # вторая полоса края для красоты
        border.goto(-x-2, y+2) # перемещение
        border.goto(x-2, y+2) # перемещение
        border.goto(x-2, -y+2) # перемещение
        border.goto(-x-2, -y+2) # перемещение
        border.goto(-x-2, y+2) # перемещение
        # третья полоса края для красоты
        border.goto(-x-4, y+4) # перемещение
        border.goto(x-4, y+4) # перемещение
        border.goto(x-4, -y+4) # перемещение
        border.goto(-x-4, -y+4) # перемещение
        border.goto(-x-4, y+4) # перемещение
        turtle.penup() # поднял карандаш
        turtle.hideturtle() # спрятал черепашку
        turtle.goto(-x+11, y+11) # перемещение
        # ниже надписи на экране
        turtle.write("Групповой проект "
                     "Сахаров, Буряк, Сыздыков, Шамсутдинов", move=False, font=("Arial", 16, "normal"))
        turtle.goto(-x+20, -y-29)
        turtle.write("Синяя еда - 3 очка, черная еда - 1 очко. "
                     "Управление змейкой стрелочками", move=False, font=("Arial", 13, "normal"))


