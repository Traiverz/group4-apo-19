import turtle
class Border():
    def __init__(self):
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.goto(-311, 311)
        border.pendown()
        border.goto(311, 311)
        border.goto(311, -311)
        border.goto(-311, -311)
        border.goto(-311, 311)
        # вторая полоса края для красоты
        border.goto(-313, 313)
        border.goto(313, 313)
        border.goto(313, -313)
        border.goto(-313, -313)
        border.goto(-313, 313)
        # третья полоса края для красоты
        border.goto(-315, 315)
        border.goto(315, 315)
        border.goto(315, -315)
        border.goto(-315, -315)
        border.goto(-315, 315)


