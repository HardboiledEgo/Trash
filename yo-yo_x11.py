# Import a library of functions called 'pygame'
import pygame
import random

from def_position import position
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen
color_box = WHITE
color_box1 = WHITE
color_box2 = WHITE
color_box3 = WHITE
color_box4 = WHITE
color_box5 = WHITE
color_box6 = WHITE
color_box7 = WHITE
color_box8 = WHITE
color_box9 = WHITE
color_box10 = WHITE
backdoor = BLACK

height_x = 1024
width_y = 920
size = (height_x, width_y)
screen = pygame.display.set_mode(size)

rect_x = random.randint(0, height_x)
rect_y = random.randint(0, width_y)
rect_x1 = random.randint(0, height_x)
rect_y1 = random.randint(0, width_y)
rect_x2 = random.randint(0, height_x)
rect_y2 = random.randint(0, width_y)
rect_x3 = random.randint(0, height_x)
rect_y3 = random.randint(0, width_y)
rect_x4 = random.randint(0, height_x)
rect_y4 = random.randint(0, width_y)
rect_x5 = random.randint(0, height_x)
rect_y5 = random.randint(0, width_y)
rect_x6 = random.randint(0, height_x)
rect_y6 = random.randint(0, width_y)
rect_x7 = random.randint(0, height_x)
rect_y7 = random.randint(0, width_y)
rect_x8 = random.randint(0, height_x)
rect_y8 = random.randint(0, width_y)
rect_x9 = random.randint(0, height_x)
rect_y9 = random.randint(0, width_y)
rect_x10 = random.randint(0, height_x)
rect_y10 = random.randint(0, width_y)
 
pygame.display.set_caption("Yo-yo")
 
# Loop until the user clicks the close button.
done = False
right_x = True
down_y = True
right_x1 = True
down_y1 = True
right_x2 = True
down_y2 = True
right_x3 = True
down_y3 = True
right_x4 = True
down_y4 = True
right_x5 = True
down_y5 = True
right_x6 = True
down_y6 = True
right_x7 = True
down_y7 = True
right_x8 = True
down_y8 = True
right_x9 = True
down_y9 = True
right_x10 = True
down_y10 = True

clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
    
    rect_x, rect_y, color_box, right_x, down_y, backdoor = position(rect_x, rect_y, color_box, height_x, width_y, right_x, down_y, backdoor)
    rect_x1, rect_y1, color_box1, right_x1, down_y1, backdoor = position(rect_x1, rect_y1, color_box1, height_x, width_y, right_x1, down_y1, backdoor)
    rect_x2, rect_y2, color_box2, right_x2, down_y2, backdoor = position(rect_x2, rect_y2, color_box2, height_x, width_y, right_x2, down_y2, backdoor)
    rect_x3, rect_y3, color_box3, right_x3, down_y3, backdoor = position(rect_x3, rect_y3, color_box3, height_x, width_y, right_x3, down_y3, backdoor)
    rect_x4, rect_y4, color_box4, right_x4, down_y4, backdoor = position(rect_x4, rect_y4, color_box4, height_x, width_y, right_x4, down_y4, backdoor)
    rect_x5, rect_y5, color_box5, right_x5, down_y5, backdoor = position(rect_x5, rect_y5, color_box5, height_x, width_y, right_x5, down_y5, backdoor)
    rect_x6, rect_y6, color_box6, right_x6, down_y6, backdoor = position(rect_x6, rect_y6, color_box6, height_x, width_y, right_x6, down_y6, backdoor)
    rect_x7, rect_y7, color_box7, right_x7, down_y7, backdoor = position(rect_x7, rect_y7, color_box7, height_x, width_y, right_x7, down_y7, backdoor)
    rect_x8, rect_y8, color_box8, right_x8, down_y8, backdoor = position(rect_x8, rect_y8, color_box8, height_x, width_y, right_x8, down_y8, backdoor)
    rect_x9, rect_y9, color_box9, right_x9, down_y9, backdoor = position(rect_x9, rect_y9, color_box9, height_x, width_y, right_x9, down_y9, backdoor)
    rect_x10, rect_y10, color_box10, right_x10, down_y10, backdoor = position(rect_x10, rect_y10, color_box10, height_x, width_y, right_x10, down_y10, backdoor)


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(backdoor)
 
    # Draw a rectangle
    pygame.draw.rect(screen, color_box, [rect_x,rect_y,150,150])
    pygame.draw.rect(screen, color_box1, [rect_x1,rect_y1,150,150])
    pygame.draw.rect(screen, color_box2, [rect_x2,rect_y2,150,150])
    pygame.draw.rect(screen, color_box3, [rect_x3,rect_y3,150,150])
    pygame.draw.rect(screen, color_box4, [rect_x4,rect_y4,150,150])
    pygame.draw.rect(screen, color_box5, [rect_x5,rect_y5,150,150])
    pygame.draw.rect(screen, color_box6, [rect_x6,rect_y6,150,150])
    pygame.draw.rect(screen, color_box7, [rect_x7,rect_y7,150,150])
    pygame.draw.rect(screen, color_box8, [rect_x8,rect_y8,150,150])
    pygame.draw.rect(screen, color_box9, [rect_x9,rect_y9,150,150])
    pygame.draw.rect(screen, color_box10, [rect_x10,rect_y10,150,150])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()