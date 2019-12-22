import math

user_request = ' '

while user_request != 'y':
    
    try:
        
        a, b, c = [int(x) for x in input('Введите коэффициэнты для уровнения вида ax^2+bx+c=y\n').split()]

        d = b**2 - 4*a*c
    
        if d<0:
            
            print('Дискриминант отрицателен, пробуй другие числа')
            exit
            
        else:
            
            x_first = ((-b) - pow(d, 0,5))/(2*a)
            x_second = ((-b) + pow(d, 0,5))/(2*a)

            print('Корни уравнения: ' + str(x_first) + ' и ' + str(x_second) + '\n')
            user_request = input("Выйти? y/n \n")
            
    except ValueError:
        
        print('Некорректные данные, попробуй ещё раз')
        exit

else:
    
    exit
