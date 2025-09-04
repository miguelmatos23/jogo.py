#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, rect
from pygame.font import Font

from codeAula.const import WINDOW_WIDTH, COLOR_RED, MENU_OPTION, COLOR_WHITE, COLOR_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('./asset/MenuAd.ogg')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=70, text="RJ", text_color=COLOR_RED, text_center_pos=((WINDOW_WIDTH / 2), 80))
            self.menu_text(text_size=70, text="Ñ É DISNEY", text_color=COLOR_RED,text_center_pos=((WINDOW_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=30, text= MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WINDOW_WIDTH / 2), 380 + 50 * i))


            pygame.display.flip()

            # Check todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechar janela
                    quit()  # fecha a janela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font = pygame.font.SysFont("comicsans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)