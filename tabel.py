user_request = ' '

while user_request != 'y':
    try:
        x,y = [int(x) for x in input("Введи последовательно основание и число с какого начинать перебор\n").split()]

        if x<1 or x>9 or y<1 or y>9:
            print('Некорректные данные, введи числа в пределах от 1 до 9')
            exit

        while y<=9:
            res = y*x
            print(str(y) + ' * ' + str(x) + ' =', end=' ')
            print(res)
    
            y+=1
            
        user_request = input('Выйти? y/n\n')
        
    except ValueError:

        print('Некорректные данные, вводить нужно только числа')
        user_request = input('Выйти? y/n\n')
        exit
