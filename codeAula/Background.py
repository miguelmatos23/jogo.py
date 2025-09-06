from codeAula.Entity import Entity
import pygame

from codeAula.const import WINDOW_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        window = pygame.display.get_surface()
        if window:  # só redimensiona se a janela existir
            self.surf = pygame.transform.scale(self.surf, window.get_size())




    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
