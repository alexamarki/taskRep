import pygame

w, h = 500, 500


class Rectangle:
    def __init__(self, topleft, bottomright):
        wid_and_hei = abs(bottomright[0] - topleft[0]), abs(bottomright[1] - topleft[1])
        if topleft[0] <= bottomright[0] and topleft[1] <= bottomright[1]:
            pass
        elif topleft[0] > bottomright[0] and topleft[1] > bottomright[1]:
            topleft = bottomright
        elif topleft[0] > bottomright[0] and topleft[1] <= bottomright[1]:
            topleft = bottomright[0], topleft[1]
        else:
            topleft = topleft[0], bottomright[1]
        self.rect = pygame.rect.Rect(*topleft, *wid_and_hei)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
                            self.rect, 5)


if __name__ == '__main__':
    pygame.init()
    sizeScreen = width, height = w, h
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Прямоугольники с Ctrl+Z')
    running = True
    saved = False
    rects = []
    saved_start = (0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION and saved:
                screen.fill((0, 0, 0))
                Rectangle(saved_start, pygame.mouse.get_pos()).draw(screen)
            elif event.type == pygame.MOUSEBUTTONDOWN and not saved:
                saved_start = pygame.mouse.get_pos()
                saved = True
            elif event.type == pygame.MOUSEBUTTONUP and saved:
                screen.fill((0, 0, 0))
                rect = Rectangle(saved_start, pygame.mouse.get_pos())
                rects.append(rect)
                saved = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_z and
                    pygame.key.get_mods() & pygame.KMOD_CTRL and
                    rects):
                    rects = rects[:-1]
                screen.fill((0, 0, 0))
        for i in range(len(rects)):
            rects[i].draw(screen)
        pygame.display.flip()
    pygame.quit()
