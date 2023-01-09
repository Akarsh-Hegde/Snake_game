import pygame
from pygame.locals import *
import time

bg_color = (31, 64, 35)
snake_color = (72, 71, 82)


class Snake:
    def __init__(self,parent_screen,x,y):
        self.screen = parent_screen      #screen is the member variable (accessible through out the class)
        self.x = x
        self.y = y
        self.dir = 'down'


    def snake_block(self):
        self.screen.fill(bg_color)      #self.screen is used here 
        pygame.draw.rect(self.screen,snake_color,(self.x,self.y,40,40))
        pygame.display.update()
    
    def moving(self):

        if self.dir == 'left':
            self.x -= 10

        if self.dir == 'right':
            self.x += 10

        if self.dir == 'up':
            self.y -= 10

        if self.dir == 'down':
            self.y += 10
        
        self.snake_block()

    def moving_left(self):
        self.dir = 'left'
    def moving_right(self):
        self.dir = 'right'
    def moving_up(self):
        self.dir = 'up'
    def moving_down(self):
        self.dir = 'down'

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.screen.fill(bg_color)
        pygame.display.flip()
        # x = 0
        # y = 0
        # self.block = Snake(self.screen,x,y)      #block is an object for Snake class
        # self.block.snake_block()     #calling snake_block function using the block object created
        

    def run(self):
        running = True
        x = 0
        y = 0
        self.mc_snake = Snake(self.screen,x,y)
        
        while running:
            
            self.mc_snake.moving()
            time.sleep(0.1)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.mc_snake.moving_left()

                    if event.key == K_RIGHT:
                        self.mc_snake.moving_right()
                        
                    if event.key == K_UP:
                        self.mc_snake.moving_up()
                        
                    if event.key == K_DOWN:
                        self.mc_snake.moving_down()
                        
                elif event.type == QUIT:
                        running = False

if __name__ == "__main__":

    game = Game()
    game.run()
    

    

    