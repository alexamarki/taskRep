import pygame
import sys
import os.path as path


class NoFileError(BaseException):
    pass


def load_image(image):
    return pygame.image.load(image)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается"]

    fon = pygame.transform.scale(load_image('data/fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


tile_images = {
    'wall': load_image('data/box.png'),
    'empty': load_image('data/grass.png')
}
player_image = load_image('data/mar.png')

tile_width = tile_height = 50

player = None

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.x, self.y = pos_x, pos_y
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, level, mover):
        if level[self.y + mover[1]][self.x + mover[0]] != '#':
            self.rect.x += mover[0] * tile_width
            self.rect.y += mover[1] * tile_height
            self.x += mover[0]
            self.y += mover[1]


def load_level(filename):
    filename = "data/" + filename
    if path.exists(filename):
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    else:
        raise NoFileError('Error: No file with the name' +
              f' {filename[5:]} found in the data directory')


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y, level


player, level_x, level_y, level = generate_level(load_level(input()))

sizeScreen = WIDTH, HEIGHT = 500, 500
FPS = 120
clock = pygame.time.Clock()
screen = pygame.display.set_mode(sizeScreen)

pygame.init()
start_screen()

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.update(level, (-1, 0))
            elif event.key == pygame.K_RIGHT:
                player.update(level, (1, 0))
            elif event.key == pygame.K_DOWN:
                player.update(level, (0, 1))
            elif event.key == pygame.K_UP:
                player.update(level, (0, -1))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

pygame.quit()
