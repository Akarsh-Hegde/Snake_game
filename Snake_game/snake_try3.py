import pygame
from pygame.locals import *
import time
import random

bg_color = (31, 64, 35)
snake_color = (72, 71, 82)
apple_color = (156, 20, 45)
size = 40

class Snake:
    def __init__(self,parent_screen,length):
        self.screen = parent_screen      #screen is the member variable (accessible through out the class)
        self.length = length
        self.x = [size]*length
        self.y = [size]*length
        self.dir = 'down'


    def snake_block(self):
        self.screen.fill(bg_color)      #self.screen is used here 
        for i in range(self.length):
            pygame.draw.rect(self.screen,snake_color,(self.x[i],self.y[i],size,size))
        pygame.display.update()
    
    def moving(self):
        for i in range(self.length-1,0,-1):     #VERY IMPORTANT- The iteration must happen from the other end of the array because it wont change its value before updating
            self.x[i] = self.x[i-1]             # If iteration starts from 1st index getting updated to 0th position then 2nd index will also be updated to 0th index position
            self.y[i] = self.y[i-1]


        if self.dir == 'left':
            self.x[0] -= size

        if self.dir == 'right':
            self.x[0] += size

        if self.dir == 'up':
            self.y[0] -= size

        if self.dir == 'down':
            self.y[0] += size
        self.snake_block()
        

    def moving_left(self):
        self.dir = 'left'
    def moving_right(self):
        self.dir = 'right'
    def moving_up(self):
        self.dir = 'up'
    def moving_down(self):
        self.dir = 'down'

class Apple:
    def __init__(self,parent_screen,x,y):
        self.screen = parent_screen
        self.x_a = x
        self.y_a = y
    
    def apple_block(self):
        pygame.draw.circle(self.screen,apple_color,(self.x_a,self.y_a),20)
        pygame.display.flip()

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
        self.x_a = 20 
        self.y_a = 20 
        self.apple = Apple(self.screen, self.x_a, self.y_a)
        
    def play(self):
        self.mc_snake.moving()
        self.apple.apple_block()

    def run(self):
        running = True
        length = 5
        self.mc_snake = Snake(self.screen,length)
        
        while running: 
            game.play()

            time.sleep(0.2)

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
    

    

    