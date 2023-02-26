import pygame

w, h = 501, 501

class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self, tick_time, pos):
        if (int(self.x), int(self.y)) == pos:
            self.x, self.y = int(self.x), int(self.y)
        else:
            if self.x < pos[0]:
                x_mod = 1
            else:
                x_mod = -1
            if self.y < pos[1]:
                y_mod = 1
            else:
                y_mod = -1
            if self.x != pos[0] and self.y != pos[1]:
                self.x += tick_time * 0.1 / (2 ** 0.5) * x_mod
                self.y += tick_time * 0.1 / (2 ** 0.5) * y_mod
            elif self.x == pos[0] and self.y != pos[1]:
                self.y += tick_time * 0.1 / (2 ** 0.5) * y_mod
            elif self.x != pos[0] and self.y == pos[1]:
                self.x += tick_time * 0.1 / (2 ** 0.5) * x_mod


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (self.x, self.y), 20)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('К щелчку')
    screen.fill((0, 0, 0))
    mouse_pos = (251, 251)
    ball = Ball(251, 251)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0, 0, 0))
        tick = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
        ball.update(tick, mouse_pos)
        ball.draw(screen)
        pygame.display.flip()

    pygame.quit()
