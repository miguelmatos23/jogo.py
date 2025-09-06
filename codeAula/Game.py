
import pygame

from codeAula.Menu import Menu
from codeAula.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from codeAula.Level import Level



class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window,'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # fechar janela
                quit()  # fecha a janela
            else:
                pass




