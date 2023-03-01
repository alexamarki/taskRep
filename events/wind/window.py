import pygame
import math

w, h = 201, 201


class Circle:
    def __init__(self, x, y, size):
        self.x, self.y = x, y
        self.size = size

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           (self.x, self.y), self.size)


class Triangle:
    def __init__(self, leftmost, rightmost):
        self.l_pos, self.r_pos = leftmost, rightmost
        self.c_pos = (101, 101)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255),
                            (self.c_pos, self.l_pos, self.r_pos))

    def update(self, alpha, pos):
        x_novel = (self.c_pos[0] + (pos[0] - self.c_pos[0])
                   * math.cos(alpha * math.pi / 180) - (pos[1] - self.c_pos[1])
                   * math.sin(alpha * math.pi / 180))
        y_novel = (self.c_pos[1] + (pos[0] - self.c_pos[0])
                   * math.sin(alpha * math.pi / 180) + (pos[1] - self.c_pos[1])
                   * math.cos(alpha * math.pi / 180))
        return x_novel, y_novel

    def batch_upd(self, alpha):
        self.l_pos = self.update(alpha, self.l_pos)
        self.r_pos = self.update(alpha, self.r_pos)


if __name__ == '__main__':
    pygame.init()
    sizeScreen = width, height = w, h
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Вентилятор')
    screen.fill((0, 0, 0))
    top = math.sin(15 * math.pi / 180) * 70
    length = math.cos(15 * math.pi / 180) * 70
    running = True
    circle = Circle(101, 101, 10)
    triangle1 = Triangle((101 - top, 101 - length),
                         (101 + top, 101 - length))
    triangle2 = Triangle((101 - top, 101 - length),
                         (101 + top, 101 - length))
    triangle3 = Triangle((101 - top, 101 - length),
                         (101 + top, 101 - length))
    triangle_array = [triangle1, triangle2, triangle3]
    triangle_array[1].batch_upd(120)
    triangle_array[2].batch_upd(-120)
    base_speed = 0
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        circle.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pressed()
                if click[0]:
                    base_speed -= 50
                elif click[2]:
                    base_speed += 50
        tick = clock.tick(120)
        for i in triangle_array:
            i.batch_upd(base_speed * tick / 1000)
            i.draw(screen)
        pygame.display.flip()
    pygame.quit()
