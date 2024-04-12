import pygame
from level import Level
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pepper Boy!")
        self.icon = pygame.image.load('../Graphics/Drafts/icon.png')
        self.tmx_maps = {0: load_pygame(join('..', 'Data', 'levels', 'omni.tmx'))}
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        dt = self.clock.tick(30) / 1000
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_stage.run(dt)
            pygame.display.update()
if __name__ == "__main__":
    game = Game()
    game.run()