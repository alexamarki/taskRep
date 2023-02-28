import pygame

w, h = 300, 400


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 30
        self.top = 30
        self.cell_size = 45

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size),
                                 not self.board[i][j])

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
            return (xcoord, ycoord)

    def on_click(self, cell):
        self.board[cell[1]][cell[0]] = not self.board[cell[1]][cell[0]]
        for i in range(self.height):
            self.board[i][cell[0]] = not self.board[i][cell[0]]
        for j in range(self.width):
            self.board[cell[1]][j] = not self.board[cell[1]][j]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Чёрное в белое и наоборот')
    screen.fill((0, 0, 0))
    board = Board(5, 7)
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
