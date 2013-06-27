
import pygame

GAME_TITLE = 'Plants VS Zombies'
WIDTH = 400
HEIGHT = 400


class Control:
    def __init__(self):
        pygame.init()
        self.screensize = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.gamestate = True
        self.mainloop()
        
    def update(self):
        pass 
        
    def mainloop(self):
        while self.gamestate:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = False
            self.update()
            pygame.display.flip()
            
if __name__ == '__main__':
    app = Control()
