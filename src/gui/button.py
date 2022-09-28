import pygame
from typing import Callable
from src.resources import resourcePath


class Button:

    def __init__(self, text: str, surface: pygame.Surface, size: tuple[int, int] = (50, 50),
                 pos: tuple[int, int] = (0, 0), callback: Callable = None,
                 callbackArgs: dict = None, fontName: str = None, fontSize: int = 30,
                 backgroundColor: tuple[int, int, int] = None, backgroundHoverColor: tuple[int, int, int] = None,
                 borderColor: tuple[int, int, int] = None, borderHoverColor: tuple[int, int, int] = None,
                 borderWidth: int = 2, textColor: tuple[int, int, int] = None,
                 textHoverColor: tuple[int, int, int] = None, focusSize: tuple[int, int] = None, ):
        self.callback = callback
        self.args = callbackArgs

        self.isSelected = False

        # Text
        self.text = text
        if text != '':
            self.fontName = fontName or f'{resourcePath}/fonts/Pixeled.ttf'
            self.smallFont = pygame.font.Font(self.fontName, fontSize-15)

        # Colors
        self.backgroundColor = backgroundColor or (200, 200, 200)
        self.backgroundHoverColor = backgroundHoverColor or (100, 100, 100)
        self.actualBackgroundColor = self.backgroundColor
        self.borderColor = borderColor or (150, 150, 150)
        self.borderHoverColor = borderHoverColor or (130, 130, 130)
        self.actualBorderColor = self.borderColor
        self.textColor = textColor or (176, 11, 85)
        self.textHoverColor = textHoverColor or (171, 205, 239)
        self.actualTextColor = self.textColor

        # Geometry
        self.borderWidth = borderWidth or 2
        self.parentSurf = surface  # Where the button will be drawn
        self.pos = pos
        self.size = size
        self.focusSize = focusSize
        self.normalSize = size
        self.rect = pygame.Rect(*pos, *size)

    def setPos(self, newPos):
        self.pos = newPos
        self.updateRect()

    def setSize(self, newSize):
        self.size = newSize
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(*self.pos, *self.size)

    @property
    def hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        self.actualBackgroundColor = self.backgroundColor
        self.actualBorderColor = self.borderColor
        self.actualTextColor = self.textColor
        if self.hover:
            if not self.isSelected:
                if self.focusSize is not None:
                    self.setSize(self.focusSize)
                self.isSelected = True
            self.actualBackgroundColor = self.backgroundHoverColor
            self.actualBorderColor = self.borderHoverColor
            self.actualTextColor = self.textHoverColor
        else:
            if self.isSelected:
                self.setSize(self.normalSize)
                self.isSelected = False

    def draw(self):
        self.update()
        # Draw background
        pygame.draw.rect(self.parentSurf, self.actualBackgroundColor, self.rect)

        # Draw border
        pygame.draw.rect(self.parentSurf, self.actualBorderColor, self.rect, self.borderWidth)

        # Draw text
        text = self.smallFont.render(self.text, True, self.actualTextColor)
        rectText = pygame.Rect(self.pos[0] + self.size[0]/2 - text.get_width()/2, self.pos[1] - 15 + self.size[1]/4, text.get_width(), text.get_height())
        self.parentSurf.blit(text, rectText)

    def clickEvent(self):
        if self.hover:
            if self.args is None:
                ret = self.callback()
            else:
                ret = self.callback(**self.args)
            return ret
