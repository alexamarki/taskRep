import pygame

w, h = 400, 400


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
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
            print(None)
        else:
            xcoord, ycoord = mouse_pos[0] - self.left, mouse_pos[1] - self.top
            xcoord //= self.cell_size
            ycoord //= self.cell_size
            print((xcoord, ycoord))


if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Я слежу за тобой!')
    screen.fill((0, 0, 0))
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_cell(pygame.mouse.get_pos())
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
