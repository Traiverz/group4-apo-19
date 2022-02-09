import turtle
class Border():
    def __init__(self, x, y):
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.goto(-x, y)
        border.pendown()
        border.goto(x, y)
        border.goto(x, -y)
        border.goto(-x, -y)
        border.goto(-x, y)
        # вторая полоса края для красоты
        border.goto(-x-2, y+2)
        border.goto(x-2, y+2)
        border.goto(x-2, -y+2)
        border.goto(-x-2, -y+2)
        border.goto(-x-2, y+2)
        # третья полоса края для красоты
        border.goto(-x-4, y+4)
        border.goto(x-4, y+4)
        border.goto(x-4, -y+4)
        border.goto(-x-4, -y+4)
        border.goto(-x-4, y+4)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-x+11, y+11)
        turtle.write("Групповой проект "
                     "Сахаров, Буряк, Сыздыков, Шамсутдинов", move=False, font=("Arial", 16, "normal"))
        turtle.goto(-x+20, -340)
        turtle.write("Синяя еда - 3 очка, черная еда - 1 очко. "
                     "Управление змейкой стрелочками", move=False, font=("Arial", 13, "normal"))


