import pygame
import copy

w, h = 700, 700


class Board:
    def __init__(self, n, bound):
        self.width = n
        self.height = n
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = bound
        self.top = bound
        self.cell_size = (w - bound * 2) / n

    def render(self, screen):
        color = (0, 255, 0)
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, color,
                                     (self.left + j * self.cell_size,
                                      self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

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


class Life(Board):
    def __init__(self, n, bound):
        super().__init__(n, bound)

    def on_click(self, cell):
        self.board[cell[1]][cell[0]] = not self.board[cell[1]][cell[0]]

    def next_move(self):
        board_cp = copy.deepcopy(self.board)
        for i in range(0, self.height):
            for j in range(0, self.width):
                back_i, back_j, forw_i, forw_j = i - 1, j - 1, i + 1, j + 1
                if back_i < 0:
                    back_i = self.height - 1
                if forw_i > self.height - 1:
                    forw_i = 0
                if back_j < 0:
                    back_j = self.width - 1
                if forw_j > self.width - 1:
                    forw_j = 0
                list_of_cells = [board_cp[back_i][back_j], board_cp[i][back_j],
                                 board_cp[forw_i][back_j], board_cp[back_i][forw_j],
                                 board_cp[i][forw_j], board_cp[forw_i][forw_j],
                                 board_cp[back_i][j], board_cp[forw_i][j]]
                if board_cp[i][j]:
                    if list_of_cells.count(1) not in (2, 3):
                        self.board[i][j] = 0
                else:
                    if list_of_cells.count(1) == 3:
                        self.board[i][j] = 1


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Жизнь на Торе')
    screen.fill((0, 0, 0))
    board = Life(40, 10)
    running = True
    started = False
    clock = pygame.time.Clock()
    delay = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not started:
                if event.button == 1:
                    board.get_click(pygame.mouse.get_pos())
                elif event.button == 3:
                    started = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                started = not started
            elif event.type == pygame.MOUSEWHEEL:
                if 0 <= delay - event.y <= 10:
                    delay -= event.y
        if started:
            clock.tick(delay)
            board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
