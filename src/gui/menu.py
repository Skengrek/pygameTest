"""
classes that define menus for a GUI
    - DropDown: a dropdown menu element containing widgets
"""

import pygame


class Dropdown:

    def __init__(self, text, surface: pygame.Surface, size: tuple[int, int] = (50, 50), pos: tuple[int, int] = (0, 0),
                 fontName: str = None, fontSize: int = 30, focusSize: tuple[int, int] = None,
                 textColor: tuple[int, int, int] = (176, 11, 85),
                 textHoverColor: tuple[int, int, int] = (171, 205, 239)):

        self.parentSurf = surface

        # Geometry
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(*self.pos, *self.size)

        # widgets
        self.widgets = []

        # Text
        self.text = text
        if text != '':
            self.fontName = fontName or './resources/fonts/Pixeled.ttf'
            self.smallFont = pygame.font.Font(self.fontName, fontSize-15)

        # Graphic
        self.normalSize = self.size
        self.focusSize = focusSize
        self.isSelected = False

        # colors:
        self.textColor = textColor
        self.textHoverColor = textHoverColor
        self.actualTextColor = self.textColor

    @property
    def hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def setPos(self, newPos):
        self.pos = newPos
        self.updateRect()

    def addWidget(self, wid, pos=None):
        if pos is not None:
            if 0 <= pos:
                self.widgets.insert(pos, wid)
        else:
            self.widgets.append(wid)

    def updateRect(self):
        self.rect = pygame.Rect(*self.pos, *self.size)

    def setSize(self, newSize):
        self.size = newSize
        self.updateRect()

    def draw(self):
        self.update()
        # Draw text
        text = self.smallFont.render(self.text, True, self.actualTextColor)

        self.setSize(text.get_size())
        rectText = pygame.Rect(self.pos[0] + self.size[0] / 2 - text.get_width() / 2,
                               self.pos[1] - 15 + self.size[1] / 4, text.get_width(), text.get_height())
        self.parentSurf.blit(text, rectText)

        if self.isSelected:
            x, y = self.pos
            x += 5
            y += self.size[1]
            width = [self.size[0]]
            for wid in self.widgets:
                wid.setPos((x, y))
                wid.draw()
                width.append(wid.size[0])
                y += wid.size[1]

            self.setSize((max(width), y))

    def clickEvent(self):
        for widget in self.widgets:
            result = widget.clickEvent()
            if result is not None:
                return result

    def update(self):
        self.actualTextColor = self.textColor
        if self.hover:
            if not self.isSelected:
                if self.focusSize is not None:
                    self.setSize(self.focusSize)
                self.isSelected = True
        else:
            if self.isSelected:
                self.setSize(self.normalSize)
                self.isSelected = False
