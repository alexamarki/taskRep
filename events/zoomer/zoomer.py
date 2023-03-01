import pygame
import copy

w, h = 501, 501


class Picture:
    def __init__(self, filename, center):
        with open(filename, 'r') as f:
            self.raw_data = f.readline()
        self.center = center
        self.data = self.raw_data.lstrip('(').rstrip(')').split('), (')
        self.array = [[float(j.replace(',', '.')) for j in i.split(';')] for i in self.data]

    def draw(self, screen, scaling):
        self.scale(scaling)
        self.image = copy.deepcopy(self.array)
        for i in range(len(self.image)):
            self.image[i][0] += self.center
            self.image[i][1] = self.center - self.image[i][1]
        pygame.draw.polygon(screen, (255, 255, 255), self.image, 1)

    def scale(self, scaling):
        for i in range(len(self.array)):
            for j in range(2):
                self.array[i][j] *= scaling


if __name__ == '__main__':
    pygame.init()
    sizeScreen = width, height = w, h
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Zoom')
    running = True
    pic = Picture('points.txt', 251)
    scale = 9
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    scale *= 1.2
                elif event.y < 0:
                    scale /= 1.2
        pic.draw(screen, scale)
        scale = 1
        pygame.display.flip()
    pygame.quit()
