import pygame
import copy

w, h = 400, 700


def not_in(item, array):
    for i in range(len(array)):
        if item in array[i]:
            return (False, (array[i].index(item), i))
    return [True]

def wave(lab, x, y, cur, n, m):
    lab[x][y] = cur
    if y + 1 < m:
        if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur):
            wave(lab, x, y + 1, cur + 1, n, m)
    if x + 1 < n:
        if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur):
            wave(lab, x + 1, y, cur + 1, n, m)
    if x - 1 >= 0:
        if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur):
            wave(lab, x - 1, y, cur + 1, n, m)
    if y - 1 >= 0:
        if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur):
            wave(lab, x, y - 1, cur + 1, n, m)
    return lab


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
            if xcoord >= self.width:
                xcoord = self.width - 1
            if ycoord >= self.height:
                ycoord = self.height - 1
            return int(xcoord), int(ycoord)

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Lines(Board):
    def __init__(self, local_w, local_h):
        super().__init__(local_w, local_h)

    def on_click(self, cell):
        not_in_data = not_in(2, self.board)
        if (((not self.board[cell[1]][cell[0]]) or
                self.board[cell[1]][cell[0]] == 2)
                and not_in_data[0]):
            self.board[cell[1]][cell[0]] = 1
        elif (self.board[cell[1]][cell[0]] == 1
              and not_in_data[0]):
            self.board[cell[1]][cell[0]] = 2
        elif (not self.board[cell[1]][cell[0]]
              and not not_in_data[0]):
            cell2 = not_in_data[1]
            if self.has_path(*cell, *cell2):
                self.board[cell2[1]][cell2[0]] = 0
                self.board[cell[1]][cell[0]] = 1

    def render(self, screen):
        color_way = [(255, 0, 0), (0, 0, 255)]
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] in (1, 2):
                    pygame.draw.circle(screen, color_way[self.board[i][j] % 2],
                                       (self.left + (j + 0.5) * self.cell_size,
                                        self.top + (i + 0.5) * self.cell_size),
                                       self.cell_size / 2, 0)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def has_path(self, x1, y1, x2, y2):
        lab = copy.deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                if lab[i][j] == 1:
                    lab[i][j] = -1
        lab = wave(lab, y1, x1, 1, self.height, self.width)
        if lab[x2][y2] > 0:
            return True
        else:
            return False





if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Линеечки')
    screen.fill((0, 0, 0))
    board = Lines(10, 15)
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
