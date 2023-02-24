import pygame

w, h = 600, 300

slider_screens = pygame.sprite.Group()


class Slider(pygame.sprite.Sprite):
    img_loc = 'data/gameover.png'

    def __init__(self):
        super().__init__(slider_screens)
        self.image = pygame.image.load(Slider.img_loc)
        self.rect = self.image.get_rect()
        self.rect.topleft = (-600, 0)
        self.movement = 200

    def update(self, tick):
        self.rect.x += self.movement * tick / 1000
        if self.rect.collidepoint(599, 299):
            self.movement = 0


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    screen.fill((0, 0, 255))
    pygame.display.set_caption('Game over')
    car = Slider()
    clock = pygame.time.Clock()
    running = True
    sliding = True
    while running:
        screen.fill((0, 0, 255))
        tick = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        slider_screens.draw(screen)
        slider_screens.update(tick)
        pygame.display.flip()
    pygame.quit()
