import pygame
from pygame.locals import *

bg_color = (39, 51, 71)

class Player:
    def __init__(self,parent_screen,icon):
        self.screen = parent_screen
        if icon in ("cross", "circle"):
            self.icon = icon
        else:
            raise ValueError("Icon should be 'cross' or 'circle' ")

    def draw(self,x,y):
        icon = pygame.image.load(f"{self.icon}.png").convert()
        self.screen.blit(icon,(x,y))
    
# class Game_over:
#     def __init__(self):
#         self.matrix = [[1,2,1],[1,1,2],[2,2,1]]

#     def update(self,x,y):
#         self.matrix[x][y] = self.block

#     def check(self):
#         for i in range(len())
#         pass

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,300))
        self.draw_table()
        self.block = [0]*9
        pygame.display.flip()

    def draw_table(self):           #draws table lines on background
        table = pygame.image.load("table.jpeg").convert()
        self.screen.blit(table,(0,0))

    def get_block(self,player):        #Get to know which Block is clicked by used
        self.valid = True
        
        if self.x in range(0,100) and self.y in range(0,100) and self.block[0] == 0:
            self.block[0] = 1
            player.draw(0,0)

        elif self.x in range(100,200) and self.y in range(0,100) and self.block[1] == 0:
            self.block[1] = 1
            player.draw(100,0)

        elif self.x in range(200,300) and self.y in range(0,100) and self.block[2] == 0:
            self.block[2] = 1
            player.draw(200,0)


        elif self.x in range(0,100) and self.y in range(100,200) and self.block[3] == 0:
            self.block[3] = 1
            player.draw(0,100)

            
        elif self.x in range(100,200) and self.y in range(100,200) and self.block[4] == 0:
            self.block[4] = 1
            player.draw(100,100)


        elif self.x in range(200,300) and self.y in range(100,200) and self.block[5] == 0:
            self.block[5] = 1
            player.draw(200,100)

        elif self.x in range(0,100) and self.y in range(200,300) and self.block[6] == 0:
            self.block[6] = 1
            player.draw(0,200)


        elif self.x in range(100,200) and self.y in range(200,300) and self.block[7] == 0:
            self.block[7] = 1
            player.draw(100,200)


        elif self.x in range(200,300) and self.y in range(200,300) and self.block[8] == 0:
            self.block[8] = 1
            player.draw(200,200)

        else:
            self.valid = False

    # def game_over(self):
    #     # matrix = [[1,2,1],[1,1,2],[2,2,1]]
    #     for i in range()

    #     pass
    
    def run(self):

        running = True
        toggle = True
        player_a = Player(self.screen, "cross")
        player_b = Player(self.screen, "circle")

        while running:
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.x,self.y = pygame.mouse.get_pos()
                    
                    if toggle:
                        print("player 1")
                        self.get_block(player_a)
                        pygame.display.update()
                        if self.valid:
                            toggle = False
                    else:
                        print("player 2")
                        self.get_block(player_b)
                        pygame.display.update()
                        if self.valid:
                            toggle = True
                
                if event.type == QUIT:
                    running = False
            


if __name__ == "__main__":
    
    game = Game()
    game.run()
    