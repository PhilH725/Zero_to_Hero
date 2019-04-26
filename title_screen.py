
""" zth title screen v1 """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

def main():

    titleScreen()


def titleScreen():

    backgroundImageOne = pygame.image.load('images/title/title1.png')
    backgroundImageTwo = pygame.image.load('images/title/title2.png')

    titleBackSurf = pygame.Surface((780, 100))
    titleBackSurf.set_alpha(45)
    titleBackRect = titleBackSurf.get_rect()
    titleBackRect.topleft = (10, 10)

    titleSurf = cfg.AR74.render('Zero to Hero', True, cfg.WHITE)
    titleRect = titleSurf.get_rect()
    titleRect.center = titleBackRect.center

    pygame.mixer.music.load('bgm/title.ogg')
    pygame.mixer.music.play(-1, 0.0)

    timer = 0
    while True:

        common_functions.standardEventHandling()

        # if timer > 40 and timer < 60:
            # cfg.DISPLAYSURF.blit(backgroundImageTwo, (0,0))
        # else:
        cfg.DISPLAYSURF.blit(backgroundImageOne, (0,0))

        cfg.DISPLAYSURF.blit(titleBackSurf, titleBackRect)
        cfg.DISPLAYSURF.blit(titleSurf, titleRect)

        timer += 1
        if timer > 200:
            timer = 0

        if cfg.mouseClicked:
            pygame.mixer.music.fadeout(500)
            return

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)





if __name__ == '__main__':
    main()
