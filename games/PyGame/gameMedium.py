import pygame
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))


#tuples for shapes
rectangle_color = (255,0,0)
rectangle_position = (350, 250)
rectangle_size = (100,100)

pygame.draw.rect(screen, rectangle_color, pygame.Rect(rectangle_position, rectangle_size))

running =  True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running =  False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    pygame.display.flip()

pygame.quit()

