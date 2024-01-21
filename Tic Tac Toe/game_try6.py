import pygame
from pygame.locals import *

bg_color = (255,255,255)

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

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,400))
        self.screen.fill(bg_color)
        self.draw_table()
        self.block = [['','',''],['','',''],['','','']]
        # self.block = [[0]*3]*3
        print(self.block)
        pygame.display.flip()

    def draw_table(self):           #draws table lines on background
        table = pygame.image.load("table.jpeg").convert()
        self.screen.blit(table,(0,0))

    def get_block(self,player):        #Get to know which Block is clicked by used
        self.valid = True
        if self.x in range(0,100) and self.y in range(0,100) and self.block[0][0] == '':
            self.block[0][0] = player.icon
            player.draw(5,5)

        elif self.x in range(100,200) and self.y in range(0,100) and self.block[0][1] == '':
            self.block[0][1] = player.icon
            player.draw(105,5)

        elif self.x in range(200,300) and self.y in range(0,100) and self.block[0][2] == '':
            self.block[0][2] = player.icon
            player.draw(205,5)

        elif self.x in range(0,100) and self.y in range(100,200) and self.block[1][0] == '':
            self.block[1][0] = player.icon
            player.draw(5,105)
            
        elif self.x in range(100,200) and self.y in range(100,200) and self.block[1][1] == '':
            self.block[1][1] = player.icon
            player.draw(105,105)

        elif self.x in range(200,300) and self.y in range(100,200) and self.block[1][2] == '':
            self.block[1][2] = player.icon
            player.draw(205,105)

        elif self.x in range(0,100) and self.y in range(200,300) and self.block[2][0] == '':
            self.block[2][0] = player.icon
            player.draw(5,205)

        elif self.x in range(100,200) and self.y in range(200,300) and self.block[2][1] == '':
            self.block[2][1] = player.icon
            player.draw(105,205)

        elif self.x in range(200,300) and self.y in range(200,300) and self.block[2][2] == '':
            self.block[2][2] = player.icon
            player.draw(205,205)

        else:
            self.valid = False

    def game_over(self,player):
        # matrix = [[1,1,1],[0,0,0],[1,0,1]]
        n = len(self.block)
        m = len(self.block[0])
        #column check
        for sublist in self.block:
            if all([val == player.icon for val in sublist]):
                return True
        #row check 
        for j in range(n):
            if all([self.block[i][j] == player.icon for i in range(m)]):            
                return True
        #principle diagonal 
        if all([self.block[j][j]==player.icon for j in range(m)]):
            return True
        #another diagonal
        if all([self.block[n-j-1][j]==player.icon for j in range(m)]):
                return True
        return False
    def display_player(self,player,num):
        font = pygame.font.SysFont("arial",10)
        line1 = font.render(f"Player: {num} Icon: {player.icon}",True,(10,10,10))
        self.screen.blit(line1,(5,310+(num*10)))
        # self.screen.fill(bg_color)

        pygame.display.flip()

    def display_gameover(self,player):
        # self.render_background()
        # self.screen.fill(bg_color)
        font = pygame.font.SysFont("arial",10)
        line1 = font.render(f"Player with {player.icon} Won!!",True,(10,10,10))
        self.screen.blit(line1,(5,360))
        line2 = font.render("To play again press Enter. To exit press Escape!",True,(10,10,10))
        self.screen.blit(line2,(5,380))

        pygame.display.flip()

    def reset(self):
        game = Game()
        game.run()

    def run(self):

        running = True
        toggle = True
        player_a = Player(self.screen, "cross")
        player_b = Player(self.screen, "circle")
        self.display_player(player_a,1)
        self.display_player(player_b,2)
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        self.reset()
                        pause = False

                if event.type == MOUSEBUTTONDOWN:

                    if not pause : 
                        self.x,self.y = pygame.mouse.get_pos()    
                        if toggle:
                            print("player 1")
                            self.get_block(player_a)
                            print(self.block)
                            pygame.display.update()
                            val = self.game_over(player_a)
                            if val:
                                print(val)
                                print("P1 Won!")
                                self.display_gameover(player_a)
                                pause = True
                            if self.valid:
                                toggle = False
                        else:
                            print("player 2")
                            self.get_block(player_b)
                            print(self.block)
                            pygame.display.update()
                            val = self.game_over(player_b)
                            if val:
                                print("P2 Won!")
                                print(val)
                                self.display_gameover(player_b)
                                pause = True
                            if self.valid:
                                toggle = True
                
                if event.type == QUIT:
                    running = False

            

if __name__ == "__main__":
    
    game = Game()
    game.run()
    

                # elif self.block[j][i] == 1:
                #     check = "Win"
                # elif self.block[j][j] == 1:
                #     check = "Win"