import pygame
import pygame_gui
from src.gui import Button


def call():
    return False


def startGameLoop(surface):
    """"""
    # Initialize background
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#00FF00'))

    # Initialize a button
    button = Button('GameLoop1', surface, callback=call, pos=(50, 50))
    isRunning = True
    clock = pygame.time.Clock()
    while isRunning:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                test = button.clickEvent()
                if test is not None:
                    isRunning = test

        surface.blit(background, (0, 0))

        button.draw()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game Loop')
    window_surface = pygame.display.set_mode((800, 600))

    startGameLoop(window_surface)

