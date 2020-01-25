num = int(input())

if num % 2 == 0:
    less_per = num/2
    max_per = num/2 - 1
else:
    less_per = (num-1)/2
    max_per = (num-1)/2 - 1

num_ex = 45*num + 5*less_per + 15*max_per

print(less_per, max_per, num_ex)

min = int(num_ex % 60)
hour = int(9 + (num_ex - min) / 60)

if min<10:
    min = '0'+ str(min)

###

name = 'World'
print('Hello %s !' %name)

num = 8
print('I have a %d fingers lol' %num)

###

import arcade

# Задать константы для размеров экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Открыть окно. Задать заголовок и размеры окна (ширина и высота)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Задать белый цвет фона.
# Для просмотра списка названий цветов прочитайте:
# http://arcade.academy/arcade.color.html
# Цвета также можно задавать в (красный, зеленый, синий) и
# (красный, зеленый, синий, альфа) формате.
arcade.set_background_color(255, 255, 255)

# Начать процесс рендера. Это нужно сделать до команд рисования
arcade.start_render()

# Нарисовать лицо
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Нарисовать правый глаз
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать левый глаз
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать улыбку
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, 
                        end_angle, 10)

# Завершить рисование и показать результат
arcade.finish_render()

# Держать окно открытым до тех пор, пока пользователь не нажмет кнопку “закрыть”
arcade.run()

###

def arithmetic(x, y, op):
    if op == '+':
        sum = x + y
    if op == '-':
        sum = x - y
    if op == '*':
        sum = x*y
    if op == '/' or op == ':':
        sum = x/y
    return(sum)


print(arithmetic(25, 10, ':'))

###

def bank(a, proc, years):
    res = 0
    i = 0
    while i < years:
        res = a + 0.01 * proc * a
        a = res
        i += 1
    return(res)

a = int(input('Введи сумму в банке: '))
proc = int(input('Введи процент вклада: '))
years = int(input('Введи срок вклада в годах: '))
print(bank(a, proc, years))

###

def date(day, month, year):
    third_one_day_month_list = (1, 3, 5, 7, 8, 10 ,12)
    third_day_month_list = (4, 6, 9, 11)
    if year >= 1:
        if month >= 1 and month <= 12:
            if day>=1 and day <= 28:
                return True
            elif day == 31 and month in third_one_day_month_list:
                return True
            elif day == 30 and month in third_day_month_list:
                return True
            elif day == 29 and month == 2 and ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)):
                return True
            else:
                return False
        else:
                return False
    else:
                return False

year = int(input('Введи год: '))
month = int(input('Введи месяц: '))
day = int(input('Введи день: '))
print(date(day, month, year))

###

class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.emp_count)  
  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

emp1 = Employee('Igor', 200)
emp1.display_employee()

###

def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr(ord(letter) ^ key)
    return  encript_str    
 
def xor_uncipher(str, key):
    uncript_str = ''
    for letter in str:
        uncript_str += chr(ord(letter) ^ key)
    return uncript_str
 
strg = input('Введите строку для шифрования: ')
key  = int(input('Введите ключ шифрования: '))

print( 'Оригинальная строка:\t', strg )
incr_strg = xor_cipher(strg, key)
print('Зашифрованная строка по ключу ' + str(key) + ':\t', incr_strg)
uncr_strg = xor_uncipher(incr_strg,key)
print('Расшифрованная строка по ключу ' + str(key) + ':\t', uncr_strg)
