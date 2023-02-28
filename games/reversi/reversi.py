import pygame
import random

w, h = 700, 700


class Board:
    def __init__(self, n):
        self.width = n
        self.height = n
        self.board = [[''] * self.width for _ in range(self.height)]
        self.left = 100
        self.top = 100
        self.cell_size = 500 / n
        self.player = 0
        for i in range(n):
            for j in range(n):
                self.board[i][j] = random.choice(['r', 'b'])

    def render(self, screen):
        color_way = {'r': (255, 0, 0), 'b': (0, 0, 255)}
        for i in range(self.height):
            for j in range(self.width):
                starting_point = (self.left + self.cell_size * j + 2,
                                  self.top + self.cell_size * i + 2)
                figure_size = self.cell_size - 4
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                pygame.draw.circle(screen, color_way.get(self.board[i][j]),
                                   (starting_point[0] + figure_size / 2,
                                    starting_point[1] + figure_size / 2),
                                   figure_size / 2)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        if (mouse_pos[0] < self.left or mouse_pos[1] < self.top
                or mouse_pos[0] > self.left + self.cell_size * self.width
                or mouse_pos[1] > self.top + self.cell_size * self.height):
            return None
        else:
            xcoord, ycoord = mouse_pos[0] - self.left, mouse_pos[1] - self.top
            xcoord /= self.cell_size
            ycoord /= self.cell_size
            return int(xcoord), int(ycoord)

    def on_click(self, cell):
        switcher = ''
        if self.player == 0 and self.board[cell[1]][cell[0]] == 'r':
            switcher = 'r'
            self.player = not self.player
        elif self.player == 1 and self.board[cell[1]][cell[0]] == 'b':
            switcher = 'b'
            self.player = not self.player
        if switcher:
            self.board[cell[1]][cell[0]] = switcher
            for i in range(self.height):
                self.board[i][cell[0]] = switcher
            for j in range(self.width):
                self.board[cell[1]][j] = switcher

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Недореверси')
    screen.fill((0, 0, 0))
    board = Board(10)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(pygame.mouse.get_pos())
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
