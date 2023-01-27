import pygame
from pygame.locals import *
import time
import random
import mysql.connector as connector

config = {
    "user": "root",
    "host": "localhost"
}
db_name = "Score_Board"
table_name = "player"

class DBplayer:    
    def __init__(self):
        self.con = connector.connect(**config)

        #create database
        query = f'create database if not exists {db_name}'
        self.cur = self.con.cursor()
        self.cur.execute(query)
        #use database
        self.cur.execute(f'use {db_name}')
        #create table
        query = f'create table if not exists {table_name} (user_id int not null auto_increment, userName varchar(50) not null, highScore int,PRIMARY KEY (user_id))'
        self.cur.execute(query)
        print(f'Database {db_name} created, Table {table_name} created')
    
    # def insert_user(self, user_name,high_score):
    #     self.query = f"insert into {table_name}(userName,highScore) values ('{user_name}',{high_score})"
    #     print(self.query)
    #     self.cur.execute(self.query)
    #     self.con.commit()
    #     print("Player saved to db...")

    def fetch(self):
        self.cur.execute(f'use {db_name}')
        query = f"select MAX(highScore) from {table_name}"
        self.cur.execute(query)
        highscore = self.cur.fetchone()
        return highscore
    
    def update(self,username,score):
        self.cur.execute(f'use {db_name}')
        query = f"select MIN(highScore) from {table_name}"
        self.cur.execute(query)
        min_score = self.cur.fetchone()
        if min_score[0] < score:
            print(min_score[0],score)
            query = f"update {table_name} set userName = '{username}', highScore = '{score}' where highScore =(select MIN(highScore) from {table_name})"
            self.cur.execute(query)

        query = f"select * from {table_name}"
        self.cur.execute(query)
        players = self.cur.fetchall()
        return players


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

        if self.snake_speed > 0.1 and self.length % 5 == 0 :
            self.snake_speed -= 0.005


    def snake_block(self):
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
        pygame.draw.circle(self.screen,apple_color,(self.x_a+20 ,self.y_a+20),20)

    def move(self):
        self.x_a = random.randint(1,24)*size
        self.y_a = random.randint(1,19)*size 
    
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.play_background_music()
        self.screen = pygame.display.set_mode((1000,800))
        # self.block = Snake(self.screen,x,y)      #block is an object for Snake class
        # self.block.snake_block()     #calling snake_block function using the block object created
        self.x_a = random.randint(1,24)*size
        self.y_a = random.randint(1,19)*size 
        self.apple = Apple(self.screen, self.x_a, self.y_a)
    
    def input_name(self):
        base_font = pygame.font.Font(None, 32)
        user_text = ''
        input_rect = pygame.Rect(450, 450, 120, 32)
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('chartreuse4')
        color = color_passive
        active = False
        while True:
            for event in pygame.event.get():
        
            # if user types QUIT then the screen will close
                if event.type == pygame.QUIT:
                    pygame.quit()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
        
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:        
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    
    
            if active:
                color = color_active
            else:
                color = color_passive
            
            pygame.draw.rect(self.screen, color, input_rect)
  
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(120, text_surface.get_width()+10)
            pygame.display.flip()

    #########################################################################
    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.screen.blit(bg, (0,0))

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)
    
    def play_sound(self, sound_name):
        if sound_name == "apple_munch":
            sound = pygame.mixer.Sound("resources/apple_munch.mp3")
        elif sound_name == "fire_sound":
            sound = pygame.mixer.Sound("resources/fire_sound.mp3")

        pygame.mixer.Sound.play(sound)
    #########################################################################
    
    def is_collision(self,x2,y2,x1,y1):     #(x2,y2)= corrodinates of snake head
        if x1 >= x2 and x1 < x2+size:
            if y1 >= y2 and y1 < y2+size:
                return True
        return False
    
    def out_of_bound(self,x,y):
        if x > 1000:
            x=0
            return x,y
        elif x < 0:
            x=1000
            return x,y
        elif y > 800:
            y=0
            return x,y
        elif y < 0:
            y=800
            return x,y 
        else:
            return x,y     
    
    def display_score(self):
        self.score = self.mc_snake.length*10 - 30  # 30 => inital_snake_length*10
        font = pygame.font.SysFont('arial',22)
        score = font.render(f"Score: {self.score}",True,(200,200,200))
        self.screen.blit(score,(850,10))
    
    def display_highscore(self):

        highscore = self.database.fetch()
        font = pygame.font.SysFont('arial',22)
        score = font.render(f"Highscore: {highscore[0]}",True,(200,200,200))
        self.screen.blit(score,(850,30))

    def play(self):
        self.render_background()
        self.mc_snake.moving()
        self.apple.apple_block()
        self.display_score()
        self.display_highscore()
        pygame.display.flip()

        time.sleep(self.mc_snake.snake_speed)
        # print(self.mc_snake.snake_speed)
        #collision with apple
        if self.is_collision(self.mc_snake.x[0],self.mc_snake.y[0],self.apple.x_a,self.apple.y_a):
            print("collision!")
            self.play_sound("apple_munch")
            self.mc_snake.increase_length()
            self.apple.move()
        
        #collision with itself
        for i in range(3,self.mc_snake.length):
            if self.is_collision(self.mc_snake.x[0],self.mc_snake.y[0],self.mc_snake.x[i],self.mc_snake.y[i]):
                self.play_sound("fire_sound")
                raise "Exception" 
        
        self.mc_snake.x[0],self.mc_snake.y[0] = self.out_of_bound(self.mc_snake.x[0],self.mc_snake.y[0])    

    def display_gameover(self):

        self.render_background()
        self.screen.fill(bg_color)
        font = pygame.font.SysFont("arial",30)
        line1 = font.render(f"Game is over! Your score is {self.score}",True,(255,255,255))
        self.screen.blit(line1,(280,300))
        line2 = font.render("To play again press Enter, To exit press Escape",True,(255,255,255))
        self.screen.blit(line2,(200,350))
        line3 = font.render("To view Score Board enter name and press Return!",True,(255,255,255))
        self.screen.blit(line3,(260,400))
        
        username = self.input_name()
        print(username)
        player_info = self.database.update(username,self.score)
        for i in player_info:
            print(i)
        pygame.display.flip()

    def reset(self):
        
        self.mc_snake = Snake(self.screen,3)
        self.apple = Apple(self.screen, self.x_a, self.y_a)

    def run(self):
        running = True
        pause = False
        direction = "y_axis"        #issue: sometimes does not reset on game restart 

        self.mc_snake = Snake(self.screen,3)
        self.database = DBplayer()
        # self.display_highscore()

        while running: 
            try:
                if not pause:
                    self.play()

            except Exception as ex:
                self.display_gameover()
                pause = True
                self.reset()
                direction = "y_axis"        #issue solved ig

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                    
                    if not pause:
                        if direction == "y_axis":
                            if event.key == K_LEFT:
                                self.mc_snake.moving_left()
                                direction = "x_axis"
                            elif event.key == K_RIGHT:
                                self.mc_snake.moving_right()
                                direction = "x_axis"
                        if direction == "x_axis":
                            if event.key == K_UP:
                                self.mc_snake.moving_up()
                                direction = "y_axis"
                            elif event.key == K_DOWN:
                                self.mc_snake.moving_down()
                                direction = "y_axis"

                elif event.type == QUIT:
                            running = False

if __name__ == "__main__":

    game = Game()
    game.run()
