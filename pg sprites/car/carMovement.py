import pygame

w, h = 600, 95

cars = pygame.sprite.Group()


class Car(pygame.sprite.Sprite):
    img_loc = 'data/car2.png'

    def __init__(self):
        super().__init__(cars)
        self.image = pygame.image.load(Car.img_loc)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.movement = 1

    def update(self):
        print(self.movement)
        self.rect = self.rect.move(self.movement, 0)
        if ((self.rect.collidepoint((599, 94)) and self.movement == 1) or (
                self.rect.collidepoint((0, 0)) and self.movement == -1)):
            self.movement = -self.movement
            self.image = pygame.transform.flip(self.image, True, False)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Машинка')
    car = Car()
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        cars.draw(screen)
        cars.update()
        pygame.display.flip()
    pygame.quit()
