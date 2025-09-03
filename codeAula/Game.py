import pygame

from codeAula.Menu.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check todos os eventos
            #for event in pygame.event.get():
               # if event.type == pygame.QUIT:
                   # pygame.quit()  # fechar janela
                    #quit()  # fecha a janela
