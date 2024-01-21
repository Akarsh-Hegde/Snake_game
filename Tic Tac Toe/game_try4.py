import pygame
from pygame.locals import *

bg_color = (39, 51, 71)

class Player:
    def __init__(self,parent_screen):
        self.screen = parent_screen
        

    def draw_cross(self,x_c,y_c):
        cross = pygame.image.load("cross.png").convert()
        self.screen.blit(cross,(x_c,y_c))
    
    def draw_circle(self,x_o,y_o):
        circle = pygame.image.load("circle.jpeg").convert()
        self.screen.blit(circle,(x_o,y_o))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,300))
        self.draw_table()
        
        pygame.display.flip()

    def draw_table(self):       #draws table lines on background
        table = pygame.image.load("table.jpeg").convert()
        self.screen.blit(table,(0,0))

    def get_block(self,x,y):        #Get to know which Block is clicked by used
        self.block = 1
        self.x = x
        self.y = y
        if self.x in range(0,100) and self.y in range(0,100):
            self.block = 1
        if self.x in range(100,200) and self.y in range(0,100):
            self.block = 2
        if self.x in range(200,300) and self.y in range(0,100):
            self.block = 3
        if self.x in range(0,100) and self.y in range(100,200):
            self.block = 4
        if self.x in range(100,200) and self.y in range(100,200):
            self.block = 5
        if self.x in range(200,300) and self.y in range(100,200):
            self.block = 6
        if self.x in range(0,100) and self.y in range(200,300):
            self.block = 7
        if self.x in range(100,200) and self.y in range(200,300):
            self.block = 8
        if self.x in range(200,300) and self.y in range(200,300):
            self.block = 9

    def click_draw_a(self,block):
        self.block = block
        player_a = Player(self.screen)
        if self.block == 1:
            player_a.draw_circle(0,0)
        if self.block == 2:
            player_a.draw_circle(100,0)
        if self.block == 3:
            player_a.draw_circle(200,0)
        if self.block == 4:
            player_a.draw_circle(0,100)
        if self.block == 5:
            player_a.draw_circle(100,100)
        if self.block == 6:
            player_a.draw_circle(200,100)
        if self.block == 7:
            player_a.draw_circle(0,200)
        if self.block == 8:
            player_a.draw_circle(100,200)
        if self.block == 9:
            player_a.draw_circle(200,200)
    
    def click_draw_b(self,block):
        self.block = block
        player_b = Player(self.screen)
        if self.block == 1:
            player_b.draw_cross(0,0)
        if self.block == 2:
            player_b.draw_cross(100,0)
        if self.block == 3:
            player_b.draw_cross(200,0)
        if self.block == 4:
            player_b.draw_cross(0,100)
        if self.block == 5:
            player_b.draw_cross(100,100)
        if self.block == 6:
            player_b.draw_cross(200,100)
        if self.block == 7:
            player_b.draw_cross(0,200)
        if self.block == 8:
            player_b.draw_cross(100,200)
        if self.block == 9:
            player_b.draw_cross(200,200)

    # def toggle_players(self):
        
    #     print("player 1")
    #     self.click_draw_a(self.block)
    #     pygame.display.update()

    #     print("player 2")
    #     self.click_draw_b(self.block)
    #     pygame.display.update()

    def run(self):

        running = True
        toggle = True

        while running:
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.x,self.y = pygame.mouse.get_pos()
                    self.get_block(self.x,self.y)
                    
                    if toggle:
                        print("player 1")
                        self.click_draw_a(self.block)
                        pygame.display.update()
                        toggle = False
                    else:
                        print("player 2")
                        self.click_draw_b(self.block)
                        pygame.display.update()
                        toggle = True
                    
                if event.type == QUIT:
                    running = False
            


if __name__ == "__main__":
    
    game = Game()
    game.run()
    