import pygame
pygame.init()

class Paddle:
    def __init__(self, x, y,speed, h, w, rgb):
        self.x =  x
        self.y = y
        self.speed = speed
        self.h =  h
        self.w =  w
        self.rgb = rgb
        #create the paddle
        self.paddleRect =  pygame.Rect(x,y,w,h)
        #put it on the screen
        self.paddle =  pygame.draw.rect(screen, self.rgb, self.paddleRect)
    def display(self):
        self.paddle =  pygame.draw.rect(screen, self.rgb, self.paddleRect)
    def update(self, yDir):
        #if yDir = 1, moving up
        #if yDir =  -1, moving down
        #if yDir = 0, not moving
        self.y = self.y + self.speed*yDir
        if self.y <0:
            self.y = 0
        elif self.y  + self.h >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.h
        self.paddleRect = (self.x, self.y, self.w, self.h)
    def getRect(self):
        return self.paddleRect

class Ball:
    pass
    def __init__(self):
        pass

SCREEN_WIDTH =  800
SCREEN_HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0, 255)
WHITE = (255,255,255)
BLACK =  (0,0,0)
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG!")

#create paddles
paddleRed =  Paddle(20, 0, 10, 100, 10, RED)
paddleBlue =  Paddle(SCREEN_WIDTH-30, 0, 10, 100, 10, BLUE)


running =  True


while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()