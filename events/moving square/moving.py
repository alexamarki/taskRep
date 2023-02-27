import pygame

w, h = 300, 300


class Square:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size = 100

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.y, self.size, self.size))

    def update(self, x_modifier, y_modifier):
        self.x += x_modifier
        self.y += y_modifier


def is_in_square(coords, square_obj):
    if ((coords[0] >= square_obj.x and coords[1] >= square_obj.y) and
            (coords[0] <= square_obj.x + square_obj.size and
             coords[1] <= square_obj.y + square_obj.size)):
        return True
    else:
        return False


if __name__ == '__main__':
    pygame.init()
    sizeScreen = width, height = w, h
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Drag')
    screen.fill((0, 0, 0))
    running = True
    square = Square(0, 0)
    not_pressed = True
    delta_x = 0
    delta_y = 0
    while running:
        screen.fill((0, 0, 0))
        square.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pressed = pygame.mouse.get_pressed()
            curr_coord = pygame.mouse.get_pos()
            if pressed[0] and is_in_square(curr_coord, square):
                if not_pressed:
                    first_coord = pygame.mouse.get_pos()
                    not_pressed = False
                    delta_x = first_coord[0] - square.x
                    delta_y = first_coord[1] - square.y
                square.update(curr_coord[0] - delta_x - square.x,
                              curr_coord[1] - delta_y - square.y)
            else:
                not_pressed = True
            pygame.display.flip()
    pygame.quit()
