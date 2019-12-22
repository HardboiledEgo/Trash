import random

def position(rect_x, rect_y, color_box, height_x, width_y, right_x, down_y, backdoor):
    
    if rect_x >= (height_x - 150):
        right_x = False
        color_box = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        backdoor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if rect_x <= 0:
        right_x = True
        color_box = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        backdoor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    if rect_y >= (width_y - 150):
        down_y = False
        color_box = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        backdoor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if rect_y <= 0:
        down_y = True
        color_box = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        backdoor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    if down_y:
        rect_y += 10
    
    else:
        rect_y -= 10
    
    if right_x:
        rect_x += 10
    
    else:
        rect_x -= 10
        
    return(rect_x, rect_y, color_box, right_x, down_y, backdoor)