import pygame
from pygame.locals import *
import time

bg_color = (31, 64, 35)
snake_color = (72, 71, 82)


class Snake:
    def __init__(self,parent_screen):
        self.screen = parent_screen      #screen is the member variable (accessible through out the class)

    def snake_block(self,x,y):
        self.screen.fill(bg_color)      #self.screen is used here 
        pygame.draw.rect(self.screen,snake_color,(x,y,40,40))
        pygame.display.update()
    
    def moving(self,x,y):
        if self.dir == 'left':
            x -= 10
        if self.dir == 'right':
            x += 10
        if self.dir == 'up':
            y -= 10
        if self.dir == 'down':
            y += 10
        
        self.snake_block(x,y)


class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1000,800))
        screen.fill(bg_color)
        pygame.display.flip()
        self.x = 0
        self.y = 0
        self.block = Snake(screen)      #block is an object for Snake class
        self.block.snake_block(self.x,self.y)     #calling snake_block function using the block object created
        self.move = Snake(screen)
        self.move.moving(self.x,self.y,'right')
        time.sleep(0.2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.move.moving(self.x,self.y,'left')

                    if event.key == K_RIGHT:
                        self.move.moving(self.x,self.y,'right')
                        
                    if event.key == K_UP:
                        self.move.moving(self.x,self.y,'up')
                        
                    if event.key == K_DOWN:
                        self.move.moving(self.x,self.y,'down')
                        
                elif event.type == QUIT:
                        running = False

if __name__ == "__main__":

    game = Game()
    game.run()
    

    

    