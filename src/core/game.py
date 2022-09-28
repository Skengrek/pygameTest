import os
from src.resources import resourcePath


class Cell:

    def __init__(self, _type, x, y):
        self.x, self.y = x, y
        self.type = _type


class Map:

    def __init__(self, file=None):

        self.cells = None

        if file is not None:
            self.importTxtMap(file)

    def importTxtMap(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        self.cells = []

        y = 0
        for line in lines:
            x = 0
            self.cells.append([])
            for cell in line.strip():
                self.cells[-1].append(Cell(cell, x, y))
                x += 1
            y += 1


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Test
if __name__ == '__main__':
    path = os.path.join(resourcePath, 'maps', 'map.txt')
    Map(path)
