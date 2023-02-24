import pygame

w, h = 300, 300
img_loc = 'data/creature.png'

if __name__ == '__main__':
    pygame.init()
    size_screen = width, height = w, h
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption('Герой двигается!')
    character = pygame.image.load(img_loc).convert_alpha()
    character_rect = character.get_rect()
    character_rect.topleft = (0, 0)
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    character_rect.y += 10
                elif event.key == pygame.K_UP:
                    character_rect.y -= 10
                elif event.key == pygame.K_RIGHT:
                    character_rect.x += 10
                elif event.key == pygame.K_LEFT:
                    character_rect.x -= 10
        screen.blit(character, character_rect)
        pygame.display.flip()
    pygame.quit()
