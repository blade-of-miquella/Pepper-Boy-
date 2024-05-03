import pygame
from level import Level
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.FULLSCREEN)
        pygame.display.set_caption("Pepper Boy!")
        self.tmx_maps = {0: load_pygame(join('..', 'Data', 'levels', 'map.tmx'))}
        self.clock = pygame.time.Clock()
        self.import_assets()
        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            'a': import_folder('..', 'Graphics', 'level', 'buttons', 'a'),
            'd': import_folder('..', 'Graphics', 'level', 'buttons', 'd'),
            's': import_folder('..', 'Graphics', 'level', 'buttons', 's'),
            'space': import_folder('..', 'Graphics', 'level', 'buttons', 'space')
        }

    def run(self):
        dt = self.clock.tick(30) / 1000
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    break
                    pygame.quit()
                    sys.exit()
            self.current_stage.run(dt)
            pygame.display.update()
            self.clock.tick(30)
if __name__ == "__main__":
    game = Game()
    game.run()