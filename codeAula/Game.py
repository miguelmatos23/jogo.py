import pygame

from codeAula.Menu import Menu
from codeAula.const import WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass


