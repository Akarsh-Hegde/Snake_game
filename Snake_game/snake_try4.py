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
        self.snake_speed = 0.2

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        # self.snake_speed -= 0.001

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
        pygame.draw.circle(self.screen,apple_color,(self.x_a ,self.y_a),20)
        pygame.display.flip()

    def move(self):
        self.x_a = random.randint(1,25)*size
        self.y_a = random.randint(1,19)*size 

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
        self.x_a = random.randint(1,25)*size
        self.y_a = random.randint(1,19)*size 
        self.apple = Apple(self.screen, self.x_a, self.y_a)
    
    def is_collision(self,x2,y2,x1,y1):     #(x2,y2)= corrodinates of snake head
        if x1 >= x2 and x1 <= x2+size:
            if y1 >= y2 and y1 <= y2+size:
                return True
        return False
    
    def display_score(self):
        font = pygame.font.SysFont('arial',22)
        score = font.render(f"Score: {self.mc_snake.length*10}",True,(200,200,200))
        self.screen.blit(score,(850,10))

    def play(self):
        self.mc_snake.moving()
        self.apple.apple_block()
        self.display_score()
        pygame.display.flip()

        time.sleep(self.mc_snake.snake_speed)
        # print(self.mc_snake.x[0],self.mc_snake.y[0],self.apple.x_a,self.apple.y_a)
        #collision with apple
        if self.is_collision(self.mc_snake.x[0],self.mc_snake.y[0],self.apple.x_a,self.apple.y_a):
            print("collision!")
            self.mc_snake.increase_length()
            self.apple.move()
        
        #collision with itself
        for i in range(3,self.mc_snake.length):
            if self.is_collision(self.mc_snake.x[0],self.mc_snake.y[0],self.mc_snake.x[i],self.mc_snake.y[i]):
                print("Game over")
                exit(0)

    def run(self):
        running = True
        self.mc_snake = Snake(self.screen,3)
        
        while running: 

            self.play()

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
    

    

    