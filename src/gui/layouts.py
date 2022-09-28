"""
Classes that define layouts of GUI elements.
    - VLayout and HLayout are vertical or horizontal layout
        where widgets are just following each others
"""

import pygame


class Layout:

    def __init__(self, pos: tuple[int, int] = None, contentSpacing: int = 5):
        self.pos = pos or (0, 0)

        self.widgets = []
        self.topMargin = 5
        self.leftMargin = 5
        self.bottomMargin = 5
        self.rightMargin = 5
        self.contentSpacing = contentSpacing
        self.rect = pygame.Rect(*self.pos, 50, 50)

    def setMargin(self, top=5, left=5, bottom=5, right=5):
        self.topMargin = top
        self.leftMargin = left
        self.bottomMargin = bottom
        self.rightMargin = right

    def addWidget(self, wid, pos=None):
        if pos is not None:
            if 0 <= pos:
                self.widgets.insert(pos, wid)
        else:
            self.widgets.append(wid)

    def draw(self):
        """Draw all the elements of this layout"""
        raise NotImplementedError

    def update(self):
        for widget in self.widgets:
            widget.update()

    def clickEvent(self):
        for widget in self.widgets:
            result = widget.clickEvent()
            if result is not None:
                return result


class VLayout(Layout):

    def draw(self):
        x = self.pos[0]
        y = self.topMargin
        width = []
        for widget in self.widgets:
            widget.setPos((x, y))
            y += widget.size[1] + self.contentSpacing
            width.append(widget.size[0])
            widget.draw()
        self.rect = pygame.Rect(*self.pos, max(width), y)


class HLayout(Layout):

    def draw(self):
        y = self.pos[1]
        x = self.topMargin
        height = []
        for widget in self.widgets:
            widget.setPos((x, y))
            x += widget.size[0] + self.contentSpacing
            height.append(widget.size[0])
            widget.draw()
        self.rect = pygame.Rect(*self.pos, x, max(height))
