import pygame

w, h = 586, 316


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 8
        self.top = 8
        self.cell_size = 30
        self.player = 0

    def render(self, screen):
        color_way = [(255, 0, 0), (0, 0, 255)]
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                if self.board[i][j]:
                    starting_point = (self.left + self.cell_size * j + 3,
                                      self.top + self.cell_size * i + 3)
                    figure_size = self.cell_size - 6
                    if self.board[i][j] == 'X':
                        pygame.draw.line(screen, color_way[1], starting_point,
                                         (starting_point[0] + figure_size,
                                          starting_point[1] + figure_size), 2)
                        pygame.draw.line(screen, color_way[1],
                                         (starting_point[0],
                                          starting_point[1] + figure_size),
                                         (starting_point[0] + figure_size,
                                          starting_point[1]), 2)
                    else:
                        pygame.draw.circle(screen, color_way[0],
                                           (starting_point[0] + figure_size / 2,
                                            starting_point[1] + figure_size / 2),
                                           figure_size / 2, 2)

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
            xcoord //= self.cell_size
            ycoord //= self.cell_size
            return xcoord, ycoord

    def on_click(self, cell):
        if not self.board[cell[1]][cell[0]]:
            if not self.player:
                self.board[cell[1]][cell[0]] = 'X'
            else:
                self.board[cell[1]][cell[0]] = 'O'
            self.player = not self.player

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Пра-пра-пра-крестики-нолики')
    screen.fill((0, 0, 0))
    board = Board(19, 10)
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
