import pygame

width, height = 500, 500
all_sprites = pygame.sprite.Group()
squares = pygame.sprite.Group()
platforms = pygame.sprite.Group()


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.sized = 20
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.add(squares)

    def update(self, tick):
        if not pygame.sprite.spritecollideany(self, platforms):
            self.rect.y += 1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((50, 10))
        self.image.fill(pygame.Color('gray'))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.add(platforms)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Платформы')
    clock = pygame.time.Clock()
    running = True
    square = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and squares:
                    square.rect.x -= 10
                elif event.key == pygame.K_RIGHT and squares:
                    square.rect.x += 10
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Platform(*pygame.mouse.get_pos())
                elif event.button == 3:
                    if not squares:
                        square = Square(*pygame.mouse.get_pos())
                    else:
                        square.rect.x, square.rect.y = pygame.mouse.get_pos()
        tick = clock.tick(50)
        squares.update(tick)
        screen.fill((0, 0, 0))
        squares.draw(screen)
        platforms.draw(screen)
        pygame.display.flip()
    pygame.quit()
