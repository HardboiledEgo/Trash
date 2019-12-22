### ИМПОРТ ВСЕХ РАБОЧИХ ЛИБ И ФУНКЦИЙ ###
import pygame # Игровая либа

### НАСТРОЙКИ, ПЕРЕМЕННЫЕ И КОНСТАНТЫ ###
# Инициализация контстант цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVY_BLUE = (0, 0, 128)
OLIVA = (128, 128, 0)
PURPLE = (128, 0, 128)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)

# Настройки экрана и отображения на экране
background_color = WHITE # Цвет фона
window_width_x = 800 # Ширина окна
window_height_y = 600 # Высота окна
fps = 60 # Установка количества итераций отрисовки главного экрана в секунду
window_name = 'minimalizm' # Имя окна

# Инициализация меню
menu_width_x = 200
menu_height_y = 300
menu_start_pos_x = (window_width_x-menu_width_x)/2
menu_start_pos_y = (window_height_y-menu_height_y)/2
menu_color = SILVER

### УСТАНОВКА ПАРАМЕТРОВ ПЕРЕД ГЛАВНЫМ ЦИКЛОМ ###
# Инициализация движка
pygame.init()

# Подключение функций библиотеки Pygame
window_size = (window_width_x, window_height_y) # Инициализация размера рабочего окна
main_screen = pygame.display.set_mode(window_size) # Инициализация переменной screen как главной рабочей области, привязка размера окна
pygame.display.set_caption(window_name) # Наименование в шапке окна

# Инициализация флагов
close_button = False # Флаг главной петли, работает пока не будет нажата кнопка закрытия окна
menu_status = False

# Инициализация переменной tick_rate, количество тиков в секунду (фпс)
tick_rate = pygame.time.Clock()

### ГЛАВНЫЙ ЦИКЛ ###
# Главная петля, логически то же самое что и while done == False (пока не нажат крестик окна)
while not close_button:
    # Запуск цикла pygame для регистрации input устройств
    for event in pygame.event.get():  # Когда юзер что-то делает
        if event.type == pygame.QUIT:  # Когда нажимает крестик
            close_button = True  # Флаг close_button становится True, следовательно следующий цикл не начнётся
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if menu_status == False:
                    menu_status = True
                else:
                    menu_status = False

    # Очистка окна и отрисовка фона
    main_screen.fill(background_color)
    
    # Игровая логика
    
    # Здесь отрисовываем наши объекты
    if menu_status:
        pygame.draw.rect(main_screen, menu_color, (menu_start_pos_x, menu_start_pos_y, menu_width_x, menu_height_y))

    # Update окна в конце отрисовки логики
    # Данная команда ОБЯЗАНА выполняться после всех команд логики и отрисовки, иначе изменения не отобразятся
    pygame.display.flip()
 
    # Последний параметр управляет fps, или количеством итераций главного цикла за секунду
    # Оставь значение в скобках пустым и программа будет использовать весь ЦП который будет доступен
    tick_rate.tick(fps)

### КОНЕЦ ПРОГРАММЫ ###
# После выполнения цикла, когда close_button = True (был нажат крестик), закрыть модуль Pygame, следовательно  закрыть окно и всю пограмму
pygame.quit()