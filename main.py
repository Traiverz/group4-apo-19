import time # библиотека времени
import turtle # библиотека черепашки
import border # внешняя библиотека с классом бордер
import smile # внешняя библиотека с классом смайл
import math # математическая библиотека
from random import randrange # библиотека случайных чисел

# после подключения библиотек переходим к созданию окна программы и определения главных составляющих

print("Правила игры: ")
print('На поле будет находиться еда в движении и без движения')
print('При поедании еды без движения вы получите 1 очко')
print('При поедании еды в движении вы получите сразу 3 очка')
print('Игра бесконечна и закончится проигрышем')

# создание окна программы
BREAK_FLAG = False # создает новую булеву переменную
screen = turtle.Screen() # создает объект типа Turtle наследуя класс(окно программы)
screen.title('Змейка: Сахаров, Буряк, Шамсутдинов, Сыздыков') # задает название окна
screen.bgcolor('gold') # задаем цвет заднего фона
screen.setup(650, 650) # определяем размер окна
screen.tracer(0) # отключаем анимацию отрисовки черепашкой объектов


# создание объекта который будет двигаться по математической формуле
cherepaha = turtle.Turtle() # создаем свободную черепаху на поле
cherepaha.color('green') # задаем ей зелёный цвет
X_cor = cherepaha.xcor() # новая переменная, содержащая координату Х нашей черепашки
Y_cor = cherepaha.ycor() # новая переменная, содержащая координату У нашей черепашки
cherepaha.penup() # поднимаем карандаш отрисовки
cherepaha.goto(-300, 0) # перемещаем черепаху по координатам
k=-300 # ещё одна переменная которая понадобится в цикле

ball = turtle.Turtle() # ещё один объект просто шарик
ball.shape('circle') # в виде круга
ball.color('blue')
ball.penup() # поднимаем карандаш
dx = 5 # прирост по Х (движение)
dy = 7 # прирост по У (движение )
randx = randrange(-300, 300)
randy = randrange(-300, 300)
ball.goto(randx, randy) # случайное появление в рандомном месте шарика

# отрисовка игровой карты, нужных переменных и змейки
bord = border.Border() # создаем поля игровой карты через обращение к внешнему классу(файл border.py)
tre = smile.Trey() # создаем треугольники в центре через обращение к внешнему классу(файл smile.py)
score = 0 # переменная в которую будет записываться результат испытания
snake = [] # создание массива который будет являться змейкой(содержать множество элементов змейки)
# элементами змейки будут являться голова и тело змейки, в результат записывается количество элементов
# тела змейки после второго (по умолчанию голова и 2 элемента тела)
for i in range(3): # массив обработки первоначальной змейки
    snake_segment = turtle.Turtle() # обработка элемента змейки
    snake_segment.shape('square') # задаем элементу змейки форму квадрата
    snake_segment.color('red') # тут будет определяться цвет нового элемента
    snake_segment.penup() # поднимаем карандаш
    if i > 0: # условие обработки определения голова это или часть тела змейки
        snake_segment.color('green') # если голова - ничего не делаем, если тело - перекрашиваем в зеленый цвет
    # определение идет следующим образом - голова змейки имеется нулевой номер, остальные 1 и выше
    snake.append(snake_segment) # добавляем новый элемент в массив, дополняя змейку

food = turtle.Turtle() # создаем переменную которая будет являться едой типа черепашка
food.shape('circle') # задаем ей вид шара
food.penup() # поднимаем карандаш
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20)) # перемещаем в рандомные координаты

screen.onkeypress(lambda: snake[0].setheading(90), 'Up') # обработка события, по нажатию клавиш с клавиатуры для змейки (вверх)
screen.onkeypress(lambda: snake[0].setheading(270), 'Down') # обработка события, по нажатию клавиш с клавиатуры для змейки (вниз)
screen.onkeypress(lambda: snake[0].setheading(180), 'Left') # обработка события по нажатию клавиш с клавиатуры для змейки (влево)
screen.onkeypress(lambda: snake[0].setheading(0), 'Right') # обработка события по нажатию клавиш с клавиатуры для змейки (вправо)
screen.listen() # считывание нажатия на клавишу

while True: # бесконечный массив с обработкой случаев выхода из него
    x, y = ball.position()  # позиция
    if x + dx >= 295 or x + dx <= -295:  # обработка отскока
        dx = -dx  # переворачиваем прирост в обратное направление
    if y + dy >= 295 or y + dy <= -295:  # так же только по координате У
        dy = -dy  #
    ball.goto(x + dx, y + dy)  # перемещение шарика

    # обработка поедания змеёй шарика
    if snake[0].distance(ball) < 15:
        ball.goto(randrange(-300, 300), randrange(-300, 300))  # шарик переходит в новое место
        for i in range(3):
            snake_segment = turtle.Turtle()  # новый элемент змейки
            snake_segment.shape('square')  # в виде квадрата
            snake_segment.color('green')  # зелёного цвета
            snake_segment.penup()  # поднимаем карандаш
            snake.append(snake_segment)  # добавляем этот элемент в массив змейки (увеличивая ее размер)
        score = score + 3  # добавляем три очка в результат

    # движение тела змеи
    for i in range(len(snake) - 1, 0, -1):  # перебираем все элементы змейки
        x = snake[i - 1].xcor()  # определяем новую координату Х
        y = snake[i - 1].ycor()  # определяем новую координату У
        snake[i].goto(x, y)  # двигаем на новую координату

    # обработка движения головы змеи
    snake[0].forward(20)  # голова змеи двигается на 20 пикс
    screen.update()  # обновляем экран

    # обработка положения головы змеи относительно краёв карты
    x_cor = snake[0].xcor()  # переменная с координатой Х головы змеи
    y_cor = snake[0].ycor()  # переменная с координатой У головы змеи
    if x_cor > 300 or x_cor < -300:  # если уходит за края карты
        x_cor = x_cor * -1  # задаем новую координату
        snake[0].goto(x_cor, y_cor)  # и она появляется с другой стороны
    if y_cor > 300 or y_cor < -300:  # если уходит за края карты
        y_cor = y_cor * -1  # задаем новую координату
        snake[0].goto(x_cor, y_cor)  # и она появляется с другой стороны

    # обработка поедания змеёй еды
    if snake[0].distance(food) < 10: # если расстояние от головы до еды меньше 20:
        food.goto(randrange(-300, 300), randrange(-300, 300)) # еда переходит в новое место
        snake_segment = turtle.Turtle() # новый элемент змейки
        snake_segment.shape('square') # в виде квадрата
        snake_segment.color('green') # зелёного цвета
        snake_segment.penup() # поднимаем карандаш
        snake.append(snake_segment) # добавляем этот элемент в массив змейки (увеличивая ее размер)
        score = score + 1 # добавляем одно очко в результат

    # обработка если змейка съест сама себя
    for i in snake[1:]: # перебираем элементы змейки
        i = i.position() # задаем переменную с расположением каждого элемента
        if snake[0].distance(i) < 10: # если змея съедает часть своего тела
            BREAK_FLAG = True # переменная созданная вначале переходит в активное состояние

    # обработка булевой переменной
    if BREAK_FLAG: # если она активна
        screen.bgcolor('red') # цвет фона в красный
        print("Вы съели себя и проиграли!!!") # вывод на экран сообщения
        print("Ваш результат: ", score) # и результата
        break # остановка цикла

    # вернёмся к свободной черепашке и задаю ее движение
    X_cor = k # координата Х черепахи берёт значение переменной из начала программы
    Y_cor = math.cos(X_cor) # координата У высчитывается по математической формуле
    if X_cor > 300: # если она уходит за пределы заданных координат
        k = -300 # возвращаем обратно
    else: #
        k = k + 10 # тут происходит изменение значения переменной
    cherepaha.goto(X_cor, Y_cor) # перемещение свободный черепашки

    time.sleep(0.1) # остановка времени работы программы( так можно настроить сложность игры)

# если произошёл выход из цикла, надо чтобы окно не закрывалось сразу же
screen.mainloop() # застывание окна