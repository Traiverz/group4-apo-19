import turtle

class zmeyka:
    snake = []
    len_snake = len(snake)
    n=0
    def __init__(self):
        for i in range(3):
            snake_n = turtle.Turtle()
            snake_n.shape('square')
            snake_n.color('black')
            snake_n.penup()
            if i > 0:
                if i % 2 == 0:
                    snake_n.color('silver')
                elif i % 2 == 1:
                    snake_n.color('white')
                else:
                    snake_n.color('white')
            self.snake.append(snake_n)

    def eat(self, x, y):
        for i in range(x):
            self.n = self.n + x
        for i in range(x):
            snake_n = turtle.Turtle()
            snake_n.shape('square')
            snake_n.color("silver")
            snake_n.penup()
            if i > 0:
                if i % 2 == 0:
                    snake_n.color('silver')
                elif i % 2 == 1:
                    snake_n.color('white')
                else:
                    snake_n.color('white')
            self.snake.append(snake_n)

    def die(self, x, y):
        x.bgcolor('red')
        turtle.goto(-163, -20)
        turtle.color("gold")
        turtle.write("ВЫ ПРОИГРАЛИ!", move=False, font=("Arial", 30, "normal"))
        print('Ваш результат: ', y)
