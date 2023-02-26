import pygame
import random

w, h = 500, 500

bombs = pygame.sprite.Group()


class Bomb(pygame.sprite.Sprite):
    boom_loc = 'data/boom.png'
    bomb_loc = 'data/bomb.png'

    def __init__(self):
        super().__init__(bombs)
        self.image = pygame.image.load(Bomb.bomb_loc)
        self.boom_image = pygame.image.load(Bomb.boom_loc)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w-100)
        self.rect.y = random.randrange(h-100)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            center = self.rect.center
            self.image = self.boom_image
            self.rect = self.image.get_rect()
            self.rect.center = center

if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Boom them all')
    for i in range(20):
        Bomb()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in bombs:
                    bomb.update(event)
        bombs.draw(screen)
        pygame.display.flip()
    pygame.quit()
