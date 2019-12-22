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
backdoor = BLACK
height_x = 800
width_y = 600
size = (height_x, width_y)
screen = pygame.display.set_mode(size)

rect_x = random.randint(0, height_x)
rect_y = random.randint(0, width_y)
 
pygame.display.set_caption("Yo-yo")
 
# Loop until the user clicks the close button.
done = False
right_x = True
down_y = True

clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
    
    rect_x, rect_y, color_box, right_x, down_y, backdoor = position(rect_x, rect_y, color_box, height_x, width_y, right_x, down_y, backdoor)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(backdoor)
 
    # Draw a rectangle
    pygame.draw.rect(screen, color_box, [rect_x,rect_y,50,50])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()