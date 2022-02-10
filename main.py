#хххххххххххххххххххххххххххххх ИМПОРТИРОВАНИЕ БИБЛИОТЕК хххххххххххххххххххххххххххххх
import time
import turtle
import border
import smile
import zmeyka
import ball
from random import randrange
#хххххххххххххххххххххххххххххх СОЗДАНИЕ ОКНА ПРОГРАММЫ хххххххххххххххххххххххххххххх
screen = turtle.Screen()
screen.title('Змейка')
screen.bgcolor('gold')
screen.setup(650, 700)
screen.tracer(0)
#хххххххххххххххххххххххххххххх СОЗДАНИЕ НЕОБХОДИМЫХ ПЕРЕМЕННЫХ хххххххххххххххххххххххххххххх
bord = border.Border(311, 311)
smile = smile.Trey()
snake = zmeyka.zmeyka()
cherepaha = ball.cherepaha(-300, 0)
#хххххххххххххххххххххххххххххх СОЗДАНИЕ ПЕРВОГО ТИПА ЕДЫ хххххххххххххххххххххххххххххх
ball1 = turtle.Turtle()
ball1.shape('circle')
ball1.color('blue')
ball1.penup()
dx = randrange(0, 10)
dy = randrange(0, 10)
randx = randrange(-300, 300)
randy = randrange(-300, 300)
ball1.goto(randx, randy)
#хххххххххххххххххххххххххххххх СОЗДАНИЕ ВТОРОГО ТИПА ЕДЫ хххххххххххххххххххххххххххххх
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.goto(randrange(-300, 300), randrange(-300, 300))

screen.onkeypress(lambda: snake.snake[0].setheading(90), 'Up') # обработка события, по нажатию клавиш с клавиатуры для змейки (вверх)
screen.onkeypress(lambda: snake.snake[0].setheading(270), 'Down') # обработка события, по нажатию клавиш с клавиатуры для змейки (вниз)
screen.onkeypress(lambda: snake.snake[0].setheading(180), 'Left') # обработка события по нажатию клавиш с клавиатуры для змейки (влево)
screen.onkeypress(lambda: snake.snake[0].setheading(0), 'Right') # обработка события по нажатию клавиш с клавиатуры для змейки (вправо)
screen.listen() # считывание нажатия на клавишу

k = -300
score = 0

while True: # бесконечный массив с обработкой случаев выхода из него
    x, y = ball1.position()  # позиция
    if x + dx >= 295 or x + dx <= -295:  # обработка отскока
        dx = -dx  # переворачиваем прирост в обратное направление
    if y + dy >= 295 or y + dy <= -295:  # так же только по координате У
        dy = -dy  #
    ball1.goto(x + dx, y + dy)  # перемещение шарика

    # движение тела змеи
    for i in range(len(snake.snake) - 1, 0, -1):  # перебираем все элементы змейки
        x = snake.snake[i - 1].xcor()  # определяем новую координату Х
        y = snake.snake[i - 1].ycor()  # определяем новую координату У
        snake.snake[i].goto(x, y)  # двигаем на новую координату

    # обработка движения головы змеи
    snake.snake[0].forward(20)  # голова змеи двигается на 20 пикс
    screen.update()  # обновляем экран

    # обработка положения головы змеи относительно краёв карты
    x_cor = snake.snake[0].xcor()  # переменная с координатой Х головы змеи
    y_cor = snake.snake[0].ycor()  # переменная с координатой У головы змеи
    if x_cor > 300 or x_cor < -300:  # если уходит за края карты
        smile.lose(1, 40, 55, 80, 95, 120, 180, 100)
        snake.die(screen, score)
        break
    if y_cor > 300 or y_cor < -300:  # если уходит за края карты
        snake.die(screen, score)
        smile.lose(1, 40, 55, 80, 95, 120, 180, 100)
        break

    # обработка поедания змеёй еды
    if snake.snake[0].distance(food) < 15: # если расстояние от головы до еды меньше 20:
        food.goto(randrange(-300, 300), randrange(-300, 300)) # еда переходит в новое место
        snake.eat(1, score)
        score = score + 1 # добавляем одно очко в результат

    if snake.snake[0].distance(ball1) < 15:
        ball1.goto(randrange(-300, 300), randrange(-300, 300))  # еда переходит в новое место
        snake.eat(3, score)
        score = score + 3

    # вернёмся к свободной черепашке и задаю ее движение
    cherepaha.pos(k) # перемещение свободный черепашки
    if k >= 300:
        k = -300
    k = k + 5
    cherepaha.dvig(screen)

    time.sleep(0.1) # остановка времени работы программы (так можно настроить сложность игры)

# если произошёл выход из цикла, надо чтобы окно не закрывалось сразу же
screen.mainloop() # застывание окна
