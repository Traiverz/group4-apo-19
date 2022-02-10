import turtle # библиотека

class zmeyka: # новый класс
    snake = [] # переменная
    len_snake = len(snake) # переменная
    n=0 # переменная
    def __init__(self): # конструктор
        for i in range(3): # цикл создания тела змейки работает 3 раза
            snake_n = turtle.Turtle() # новый объект
            snake_n.shape('square') # тип квадраи
            snake_n.color('black') # цвет черный
            snake_n.penup() # поднял карандаш
            if i > 0: # условие в котором я буду задавать цвет тела змейки
                if i % 2 == 0: # четный элемент будет цвета сильвер
                    snake_n.color('silver') # тут задаем цвет
                elif i % 2 == 1: # нечетный элемент цвета белого
                    snake_n.color('white') # задаем цвет
                else:  # иные случаи
                    snake_n.color('white') # тоже белый цвет
            self.snake.append(snake_n) # добавляем в массив

    def eat(self, x, y): # метод поедания
        for i in range(x): # добавляем х раз
            self.n = self.n + x # выполняем
        for i in range(x): #
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
