### ИМПОРТ ВСЕХ РАБОЧИХ ЛИБ И ФУНКЦИЙ ###
import pygame # Игровая либа
from math import sqrt
from def_data import *
from def_gravity import *

# Настройки экрана и отображения на экране
background = pygame.image.load('Arena.bmp')
background_color = WHITE # Цвет фона
window_width_x = hd[0] # Ширина окна
window_height_y = hd[1] # Высота окна
window_name = 'arena' # Имя окна

# Инициализация меню
menu_width_x = 200
menu_height_y = 300
menu_start_pos_x = (window_width_x-menu_width_x)/2
menu_start_pos_y = (window_height_y-menu_height_y)/2
menu_color = BLACK
button_width_x = 160
button_height_y = 80
start_button_start_pos_x = menu_start_pos_x + (menu_width_x - button_width_x)/2
start_button_start_pos_y = menu_start_pos_y + (menu_width_x - button_width_x)/2
quit_button_start_pos_x = menu_start_pos_x + (menu_width_x - button_width_x)/2
quit_button_start_pos_y = menu_start_pos_y + menu_height_y - (menu_width_x - button_width_x)/2 - button_height_y
resume_button_start_pos_x = menu_start_pos_x + (menu_width_x - button_width_x)/2
resume_button_start_pos_y = menu_start_pos_y + (menu_height_y - button_height_y)/2
start_button_color = WHITE
quit_button_color = WHITE
resume_button_color = WHITE

# Настройка игрока
player_color = BLACK

# Характеристики игрока
player_speed = 0 #Скорость передвижения
jump_level = player_y - 35
jump_time = 15
jump_limit = 1
jump_try = 1

#
ground_level = window_height_y - player_height
left_wall = 0
right_wall = window_width_x - player_width
g = 5
delta = 0
t = 0

### УСТАНОВКА ПАРАМЕТРОВ ПЕРЕД ГЛАВНЫМ ЦИКЛОМ ###
# Инициализация движка
pygame.init()

# Подключение функций библиотеки Pygame для параметров окна
window_size = (window_width_x, window_height_y) # Инициализация размера рабочего окна
main_screen = pygame.display.set_mode(window_size) # Инициализация переменной screen как главной рабочей области, привязка размера окна
pygame.display.set_caption(window_name) # Наименование в шапке окна

#
start_button_font = pygame.font.Font('freesansbold.ttf', 20)
start_button_surface = start_button_font.render('НОВАЯ ИГРА', True, BLACK)
start_button_obj = start_button_surface.get_rect()
start_button_obj.center = (start_button_start_pos_x + button_width_x/2, start_button_start_pos_y + button_height_y/2)
quit_button_font = pygame.font.Font('freesansbold.ttf', 20)
quit_button_surface = quit_button_font.render('ВЫХОД', True, BLACK)
quit_button_obj = quit_button_surface.get_rect()
quit_button_obj.center = (quit_button_start_pos_x + button_width_x/2, quit_button_start_pos_y + button_height_y/2)
resume_button_font = pygame.font.Font('freesansbold.ttf', 20)
resume_button_surface = resume_button_font.render('ПРОДОЛЖИТЬ', True, BLACK)
resume_button_obj = resume_button_surface.get_rect()
resume_button_obj.center = (resume_button_start_pos_x + button_width_x/2, resume_button_start_pos_y + button_height_y/2)

# Инициализация флагов
close_button = False # Флаг главной петли, работает пока не будет нажата кнопка закрытия окна
menu_status = True
JUMP = False

### ГЛАВНЫЙ ЦИКЛ ###
# Главная петля, логически то же самое что и while done == False (пока не нажат крестик окна)
while not close_button:
    pygame.time.delay(15)
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
            if event.key == pygame.K_LEFT:
                player_speed = -speed
            if event.key == pygame.K_RIGHT:
                player_speed = speed
            if event.key == pygame.K_UP and jump_try < jump_limit:
                JUMP = True
                jump_try += 1
                
        if event.type == pygame.MOUSEBUTTONDOWN and menu_status:
            if event.button == 1:
                if (event.pos[0] <= quit_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= quit_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= quit_button_start_pos_x) and\
                (event.pos[1] >= quit_button_start_pos_y):
                    close_button = True
                if (event.pos[0] <= resume_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= resume_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= resume_button_start_pos_x) and\
                (event.pos[1] >= resume_button_start_pos_y):
                    menu_status = False
                if (event.pos[0] <= start_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= start_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= start_button_start_pos_x) and\
                (event.pos[1] >= start_button_start_pos_y):
                    player_x = 0
                    player_y = 0
                    menu_status = False
                    
        if event.type == pygame.MOUSEMOTION and menu_status:
            if (event.pos[0] <= quit_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= quit_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= quit_button_start_pos_x) and\
                (event.pos[1] >= quit_button_start_pos_y):
                quit_button_color = SILVER
            else:
                quit_button_color = WHITE
            if (event.pos[0] <= resume_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= resume_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= resume_button_start_pos_x) and\
                (event.pos[1] >= resume_button_start_pos_y):
                resume_button_color = SILVER
            else:
                resume_button_color = WHITE
            if (event.pos[0] <= start_button_start_pos_x + button_width_x) and\
                (event.pos[1] <= start_button_start_pos_y + button_height_y) and\
                (event.pos[0] >= start_button_start_pos_x) and\
                (event.pos[1] >= start_button_start_pos_y):
                start_button_color = SILVER
            else:
                start_button_color = WHITE
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed = 0
            if event.key == pygame.K_RIGHT:
                player_speed = 0

    # Очистка окна и отрисовка фона
    main_screen.blit(background, (0,0))
    
    # Игровая логика
    if menu_status == False:
        if left_wall>player_x+player_speed:
            player_x = left_wall
            player_speed = 0
        
        if player_x+player_speed>right_wall:
            player_x = right_wall
            player_speed = 0
        
        player_x += player_speed
    
        if JUMP:
            if player_y > jump_level:
                player_y -= int(sqrt(2*g*jump_time))
                if jump_time > 0:
                    jump_time -= 1
                else:
                    jump_time = 15
                    JUMP = False

        if player_y < ground_level and not JUMP:
            player_y = gravity(player_y, ground_level, g, t)
            t += 1
        if player_y == ground_level:
            t = 0
            jump_try = 0
    
    # Здесь отрисовываем наши объекты
    pygame.draw.rect(main_screen, player_color, (player_x, player_y, player_width, player_height))
    
    if menu_status:
        pygame.draw.rect(main_screen, menu_color, (menu_start_pos_x, menu_start_pos_y, menu_width_x, menu_height_y))
        pygame.draw.rect(main_screen, start_button_color, (start_button_start_pos_x, start_button_start_pos_y, button_width_x, button_height_y))
        pygame.draw.rect(main_screen, quit_button_color, (quit_button_start_pos_x, quit_button_start_pos_y, button_width_x, button_height_y))
        pygame.draw.rect(main_screen, resume_button_color, (resume_button_start_pos_x, resume_button_start_pos_y, button_width_x, button_height_y))
        main_screen.blit(start_button_surface, start_button_obj)
        main_screen.blit(quit_button_surface, quit_button_obj)
        main_screen.blit(resume_button_surface, resume_button_obj)
        
    # Update окна в конце отрисовки логики
    # Данная команда ОБЯЗАНА выполняться после всех команд логики и отрисовки, иначе изменения не отобразятся
    pygame.display.flip()

### КОНЕЦ ПРОГРАММЫ ###
# После выполнения цикла, когда close_button = True (был нажат крестик), закрыть модуль Pygame, следовательно  закрыть окно и всю пограмму
pygame.quit()