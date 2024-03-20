import pygame
pygame.init()
class Player:
    #add color to the definition (RGB)
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self. w = w
        self.h = h
        self.speed =  speed
    
    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.w)


width = 800
height = 600
test = False

screen = pygame.display.set_mode((width, height))

player1 =  Player(250, 250, 100,100, 1)

#create a second instance of your class here
running =  True
while running:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running =  False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    keys =  pygame.key.get_pressed()
    
    dx=0
    dy=0
    if keys[pygame.K_LEFT]:
        dx-=1
    if keys[pygame.K_RIGHT]:
        dx+=1
    if keys[pygame.K_UP]:
        dy-=1
    if keys[pygame.K_DOWN]:
        dy+=1

#move that second object using WASD
        
    
    player1.move(dx, dy)
    player1.draw(screen)

    pygame.display.flip()

pygame.quit()

