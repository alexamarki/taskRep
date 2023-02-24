import pygame

w, h = 400, 300

if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Свой курсор мыши')
    screen.fill((0, 0, 0))
    cursor = pygame.image.load('arrow/data/arrow.png').convert_alpha()
    cursor_rect = cursor.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            cursor_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor, cursor_rect)
        pygame.display.flip()

    pygame.quit()
