import os
import pygame
from math import sqrt
from src.resources import resourcePath
from src.core.game import Map


class CellRenderer:

    img = {
        'X': pygame.image.load(os.path.join(resourcePath, 'imgs', 'fullBlock.png')),
        '0': pygame.image.load(os.path.join(resourcePath, 'imgs', 'halfBlock.png')),
        '1': pygame.image.load(os.path.join(resourcePath, 'imgs', 'ramp1Block.png')),
        '2': pygame.image.load(os.path.join(resourcePath, 'imgs', 'ramp2Block.png')),
    }

    tileHeight = 32
    tileWidth = 64
    mapHeight = 5
    mapWidth = 4

    def __init__(self, cell):
        self.cell = cell
        self.rect = None

    def draw(self, surface):
        x = (self.cell.x * self.tileWidth)/2 \
            + (self.mapHeight * self.cell.x)/2 \
            - (self.cell.y * self.tileWidth)/2
        y = (self.mapHeight-self.cell.y-1)*self.tileHeight/2 \
            + self.mapWidth*self.tileHeight/2 \
            - self.cell.x*self.tileHeight/2

        img = self.img[self.cell.type]
        self.rect = surface.blit(img, (x+300, y))

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

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        window_surface.blit(background, (0, 0))
        renderer.draw(window_surface)
        pygame.display.update()


