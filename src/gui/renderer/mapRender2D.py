"""
A game render in a 2D topdown view
"""
from math import floor
import os
import pygame

from src.core.map import Map
from src.core.player import Player
from src.resources import resourcePath


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
        'X': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile2.png')),
        '0': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile1.png')),
        '1': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile4.png')),
        '2': pygame.image.load(os.path.join(resourcePath, 'imgs', 'tile3.png')),
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
        self.map = _map

        self.cells = []

        for line in self.map.cells:
            mapLine = []
            for cell in line:
                mapLine.append(CellRenderer(cell))
            self.cells.append(mapLine)

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

    def cellAtPos(self, pos):
        xIndex = floor(pos[0] / 64)
        yIndex = floor(pos[1] / 64)
        if yIndex < len(self.cells) and xIndex < len(self.cells[0]):
            return self.cells[yIndex][xIndex]


class Render2D:
    """
    This class will be used to render the map in a topdown 2D view
    """

    img = {
        'hover': pygame.image.load(os.path.join(resourcePath, 'imgs', 'hoverTile.png'))
    }

    def __init__(self, _map, _player):
        self.map = _map
        self.player = _player

        self.mapRenderer = MapRenderer(self.map)
        self.playerRender = PlayerRenderer(self.player)

        self.is_running = False

    def start(self, surface):
        self.is_running = True
        hover_cell = None
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.is_running = False
                if e.type == pygame.MOUSEMOTION:
                    cell = self.mapRenderer.cellAtPos(e.pos)
                    if cell is not None:
                        hover_cell = cell
                    else:
                        hover_cell = None
                self.update(e)
            self.draw(surface)
            if hover_cell is not None:
                surface.blit(self.img["hover"], hover_cell.rect)
            pygame.display.update()

    def draw(self, surface):
        self.mapRenderer.draw(surface)
        self.playerRender.draw(surface)

    def update(self, e: pygame.event):
        """
        Update the player and the map according to events.

        Args:
            e: the pygame events.
        """
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Render test')
    window_surface = pygame.display.set_mode((800, 600))
    path = os.path.join(resourcePath, 'maps', 'map.txt')

    renderer = Render2D(Map(path), Player(1, 2))

    renderer.start(window_surface)


