import pygame
from pygame.locals import *

bg_color = (39, 51, 71)

class player:
    def __init__(self):
        pass
    


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((300,300))
        # self.screen.fill(bg_color)
        self.draw_table()
        pygame.display.flip()

    def draw_table(self):
        cross = pygame.image.load("cross.jpeg").convert()
        self.screen.blit(cross,(0,0))
        # pygame.display.flip()

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass
                
                if event.type == QUIT:
                    running = False



if __name__ == "__main__":
    
    game = Game()
    game.run()
    