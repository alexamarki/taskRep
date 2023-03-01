import pygame


def draw_cube(screen):
    start_x = 130 - (width / 2)
    start_y = 180 - (width / 2)

    color_top = pygame.Color((255, 255, 255))
    sva_top = color_top.hsva
    color_top.hsva = (hue, sva_top[1] + 100, sva_top[2], sva_top[3])
    pygame.draw.polygon(screen, color_top,
                        ((start_x + width / 2, start_y - width / 2), (start_x + width / 2 + width, start_y - width / 2),
                         (start_x + width, start_y), (start_x, start_y)))
    color_front = pygame.Color((255, 255, 255))
    sva_front = color_front.hsva
    color_front.hsva = (hue, sva_front[1] + 100, sva_front[2] - 25, sva_front[3])
    pygame.draw.polygon(screen, color_front,
                        ((start_x, start_y), (start_x + width, start_y),
                         (start_x + width, start_y + width), (start_x, start_y + width)))
    color_side = pygame.Color((255, 255, 255))
    sva_side = color_side.hsva
    color_side.hsva = (hue, sva_side[1] + 100, sva_side[2] - 50, sva_side[3])
    pygame.draw.polygon(screen, color_side,
                        ((start_x + width, start_y), (start_x + width / 2 + width, start_y - width / 2),
                         (start_x + width / 2 + width, start_y + width / 2), (start_x + width, start_y + width)))


try:
    width, hue = map(int, input().split())
    assert not width % 4
    assert 3 < width < 101
    assert 0 <= hue <= 360
except Exception:
    print('Неправильный формат ввода')
    exit()

pygame.init()
running = True
screen = pygame.display.set_mode((300, 300))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_cube(screen)
    pygame.display.flip()

pygame.quit()
