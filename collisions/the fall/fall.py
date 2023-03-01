import pygame
import pygame.image as img

width, height = 789, 400
all_sprites = pygame.sprite.Group()


class Mountain(pygame.sprite.Sprite):
    image = img.load("data/mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


mountain = Mountain()


class Landing(pygame.sprite.Sprite):
    image = img.load("data/pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((50, 45), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, (255, 0, 0), (20, 36, 9, 9))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect.y += 1


pygame.init()
size_screen = width, height
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('Десант')
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    tick = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    all_sprites.draw(screen)
    for i in all_sprites:
        i.update()
    pygame.display.flip()
pygame.quit()
