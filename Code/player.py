import sys
import time
import pygame

from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../Graphics/Drafts/pepper1.png')
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        self.speed = 40
        self.gravity = 30
        self.jump = False
        self.jump_height = 120
        self.direction = vector()

        self.collision_sprites = collision_sprites
        self.on_surface = {'floor': False, 'left': False, 'right': False}

    def input(self):
        keys  = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_d]:
            input_vector.x += 1
            self.image = pygame.image.load('../Graphics/Drafts/pepper1.png')
        elif keys[pygame.K_a]:
            input_vector.x -= 1
            self.image = pygame.image.load('../Graphics/Drafts/pepper3.png')
        else:
            input_vector.x = 0
        self.direction.x = input_vector.normalize().x if input_vector else 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump = True

        if keys[pygame.K_ESCAPE]:
            pygame.QUIT
            sys.exit()

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt
        self.collision('vertical')

        if self.jump:
            if self.on_surface['floor']:
                self.direction.y = -self.jump_height
            self.jump = False


    def check_contact(self):
        floor_rect = pygame.Rect(self.rect.bottomleft,(self.rect.width,2))
        collide_rects = [sprite.rect for sprite in self.collision_sprites]

        self.on_surface['floor'] = True if floor_rect.collidelist(collide_rects) >= 0 else False

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                if axis == 'vertical':
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        self.check_contact()