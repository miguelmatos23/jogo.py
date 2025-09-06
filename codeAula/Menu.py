#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface
from pygame.font import Font

from codeAula.const import WINDOW_WIDTH, COLOR_RED, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/MenuAd.ogg')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="RJ", text_color=COLOR_RED, text_center_pos=((WINDOW_WIDTH / 2), 40))
            self.menu_text(text_size=50, text="Ñ É DISNEY", text_color=COLOR_RED,text_center_pos=((WINDOW_WIDTH / 2), 80))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=30, text= MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WINDOW_WIDTH / 2), 160 + 50 * i))
                else:
                    self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=COLOR_WHITE,text_center_pos=((WINDOW_WIDTH / 2), 160 + 50 * i))
            pygame.display.flip()

            # Check todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechar janela
                    quit()  # fecha a janela
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #TECLAD P BAIXO
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  #TECLAD P CIMA
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font = pygame.font.SysFont("comicsans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)