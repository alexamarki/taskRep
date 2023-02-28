import pygame
import random

w, h = 400, 700


class Board:
    def __init__(self, local_w, local_h):
        bound = 10
        self.width = local_w
        self.height = local_h
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = bound
        self.top = bound
        self.cell_size = min((w - bound * 2) / self.width,
                             (h - bound * 2) / self.height)

    def render(self, screen):
        pass

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
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class MineSweeper(Board):
    def __init__(self, local_w, local_h, mines):
        super().__init__(local_w, local_h)
        self.board = [[-1] * self.width for _ in range(self.height)]
        self.font = pygame.font.Font(None, int(self.cell_size))
        for i in range(mines):
            choice = (random.randrange(self.height),
                      random.randrange(self.width))
            while self.board[choice[0]][choice[1]] == 10:
                choice = (random.randrange(self.height),
                          random.randrange(self.width))
            self.board[choice[0]][choice[1]] = 10

    def on_click(self, cell):
        self.open_cell(cell)

    def render(self, screen):
        color_way = [(255, 0, 0), (0, 255, 0)]
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 10:
                    pygame.draw.rect(screen, color_way[0],
                                     (self.left + j * self.cell_size,
                                      self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                elif self.board[i][j] != -1:
                    font_surface = self.font.render(str(self.board[i][j]),
                                                    True, color_way[1])
                    blit_rect = font_surface.get_rect()
                    blit_rect.center = (self.left + (j + 0.5) * self.cell_size,
                                        self.top + (i + 0.5) * self.cell_size)
                    screen.blit(font_surface, blit_rect)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def open_cell(self, cell):
        i, j = cell[1], cell[0]
        if self.board[i][j] == -1:
            back_i, back_j, forw_i, forw_j = i - 1, j - 1, i + 1, j + 1
            if back_i < 0:
                back_i = i
            if forw_i > self.height - 1:
                forw_i = i
            if back_j < 0:
                back_j = j
            if forw_j > self.width - 1:
                forw_j = j
            list_of_cells = [self.board[back_i][back_j], self.board[i][back_j],
                             self.board[forw_i][back_j], self.board[back_i][forw_j],
                             self.board[i][forw_j], self.board[forw_i][forw_j],
                             self.board[back_i][j], self.board[forw_i][j]]
            self.board[i][j] = list_of_cells.count(10)
            if not self.board[i][j]:
                list_of_cell_loc = [[back_j, back_i], [back_j, i],
                                    [back_j, forw_i], [forw_j, back_i],
                                    [forw_j, i], [forw_j, forw_i],
                                    [j, back_i], [j, forw_i]]
                for fi_c in list_of_cell_loc:
                    if fi_c[0] in range(self.width) and fi_c[1] in range(self.height):
                        self.open_cell(fi_c)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Папа сапёра')
    screen.fill((0, 0, 0))
    board = MineSweeper(20, 35, 50)
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
