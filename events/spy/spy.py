import pygame

w, h = 200, 200

if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Я слежу за тобой!')
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    minimised = 0
    running = True
    focus = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not pygame.key.get_focused() and focus:
                focus = False
                minimised += 1
            elif pygame.key.get_focused() and not focus:
                focus = True
        font_surface = font.render(str(minimised), True, (255, 0, 0))
        blit_rect = font_surface.get_rect()
        blit_rect.center = (100, 100)
        screen.blit(font_surface, blit_rect)
        pygame.display.flip()

    pygame.quit()
