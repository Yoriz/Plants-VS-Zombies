
import pygame

GAME_TITLE = 'Plants VS Zombies'
WIDTH = 400
HEIGHT = 400


class BallTest(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = (255, 255, 255)
        self.pos = (WIDTH // 2, HEIGHT // 2)
        self.radius = 25
        self.width = 0
        self.vel = (2, 1)
        print(self.pos)
        
    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)


class Control:
    def __init__(self):
        pygame.init()
        self.screensize = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.gamestate = True
        self.ball = BallTest(self.screen)
        self.mainloop()
        
    def update(self):
        self.ball.update()
        
    def mainloop(self):
        while self.gamestate:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = False
            self.update()
            pygame.display.flip()
            
if __name__ == '__main__':
    app = Control()
