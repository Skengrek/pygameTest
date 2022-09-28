import os
import pygame
from src.resources import resourcePath
from src.core.game import Map, Player


class PlayerRenderer:
    img = {
        'test': pygame.image.load(os.path.join(resourcePath, 'imgs', 'playerTest.png')),
    }

    def __init__(self, player):
        self.player = player
        self.rect = None

    def draw(self, surface):
        x = self.player.x * 64
        y = self.player.y * 64

        img = self.img['test']
        self.rect = surface.blit(img, (x, y))


class CellRenderer:

    img = {
        'X': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile1.png')),
        '0': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile2.png')),
        '1': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile3.png')),
        '2': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile4.png')),
    }

    tileHeight = 64
    tileWidth = 64
    mapHeight = 5
    mapWidth = 4

    def __init__(self, cell):
        self.cell = cell
        self.rect = None

    def draw(self, surface):
        x = self.cell.x * self.tileWidth
        y = self.cell.y * self.tileHeight

        img = self.img[self.cell.type]
        self.rect = surface.blit(img, (x, y))

    def update(self):
        pass


class MapRenderer:

    def __init__(self, _map):
        self.map = Map(_map)

        self.cells = []

        for line in self.map.cells:
            mapLine = []
            for cell in line:
                mapLine.append(CellRenderer(cell))
            mapLine.reverse()
            self.cells.append(mapLine)

        self.cells.reverse()

    def update(self):
        pass

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

    def events(self, e):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Render test')
    window_surface = pygame.display.set_mode((800, 600))
    path = os.path.join(resourcePath, 'maps', 'map.txt')
    renderer = MapRenderer(path)

    p = Player(1, 3)
    pr = PlayerRenderer(p)

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEMOTION:

        window_surface.blit(background, (0, 0))
        renderer.draw(window_surface)
        pr.draw(window_surface)
        pygame.display.update()


