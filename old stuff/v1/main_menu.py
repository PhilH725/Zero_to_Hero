
""" main menu screen for zth v1
        there will be a handful of unimplemented options here, im mostly just getting the screen in place. """

import pygame
import cfg, common_functions, player_class

""" ------------------------------------------------------------------------ """

def main():

    player = mainMenuScreen()


def mainMenuScreen():

    while True:
        select = None

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.fill(cfg.BLACK)

        mainMenuBackSurf = pygame.Surface((250,280))
        mainMenuBackRect = mainMenuBackSurf.get_rect()
        mainMenuBackRect.midtop = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 8)
        cfg.DISPLAYSURF.blit(mainMenuBackSurf, mainMenuBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.BLUE, mainMenuBackRect, 2)

        x = mainMenuBackRect.centerx
        y = mainMenuBackRect.top + 20
        for i in cfg.MAINMENUOPTIONS:
            optionSurf = cfg.AR28.render(i, True, cfg.WHITE)
            optionRect = optionSurf.get_rect()
            optionRect.midtop = (x, y)
            if optionRect.collidepoint(cfg.mouseX, cfg.mouseY):
                optionSurf = cfg.AR28.render(i, True, cfg.RED)
                pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (optionRect.left + 5, optionRect.bottom + 1),
                    (optionRect.right - 5, optionRect.bottom + 1), 1)
                if cfg.mouseClicked:
                    select = i
            cfg.DISPLAYSURF.blit(optionSurf, optionRect)
            y += 50

        if select == 'Quick Play':
            player = player_class.Player('Phil')
            return player

        elif select == 'New Game':
            #maybe in v2
            #player = characterCreationScreen()
            #return player
            pass

        elif select == 'Load Game':
            #long way off from this :P
            pass

        elif select == 'Options':
            pass

        elif select == 'Exit Game':
            common_functions.terminate()

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)




if __name__ == '__main__':
    main()
