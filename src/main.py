import pygame
from src.gui.widgets.menu import Dropdown
from src.gui.widgets.button import Button
from src.gui.widgets.layouts import HLayout as Layout
from core.gameloop import startGameLoop


def callBackPrint(text):
    print(text)


def changeMenu(menuName):
    return ['changeLoop', menuName]


def changeLoop(loopName, surface):
    if loopName == "gameLoop":
        startGameLoop(surface)


def menuLoop(surface):
    is_running = True
    while is_running:
        # time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                returnVal = layout.clickEvent()
                if returnVal is not None:
                    if len(returnVal) == 2:
                        if returnVal[0] == "changeLoop":
                            changeLoop(returnVal[1], window_surface)

        surface.blit(background, (0, 0))
        layout.draw()
        pygame.display.update()


if __name__ == '__main__':

    pygame.init()

    pygame.display.set_caption('Quick Start')

    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    layout = Layout((10, 10))
    layout.addWidget(Button('Hello', window_surface, size=(100, 33), pos=(5, 10), callback=callBackPrint,
                            callbackArgs={'text': "Hello"}))
    drop = Dropdown('Dropdown', window_surface, size=(200, 33))
    drop.addWidget(Button('Hello_2', window_surface, size=(100, 33), pos=(5, 10), callback=changeMenu,
                          callbackArgs={'menuName': 'gameLoop'}))
    layout.addWidget(drop)
    clock = pygame.time.Clock()
    menuLoop(window_surface)
