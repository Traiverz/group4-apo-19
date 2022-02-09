import turtle

class zmeyka:
    snake = []
    len_snake = len(snake)
    n=0
    def __init__(self):
        for i in range(3):
            snake_n = turtle.Turtle()
            snake_n.shape('square')
            snake_n.color('red')
            snake_n.penup()
            if i > 0:
                snake_n.color('green')
            self.snake.append(snake_n)

    def eat(self, x, y):
        for i in range(x):
            self.n = self.n + x
        for i in range(x):
            snake_n = turtle.Turtle()
            snake_n.shape('square')
            snake_n.color('green')
            snake_n.penup()
            self.snake.append(snake_n)

    def die(self, x, y):
        x.bgcolor('red')
        print('Ваш результат: ', y)