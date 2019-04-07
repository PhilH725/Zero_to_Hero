
""" location class for zth """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """
# location class

class Location():
    def __init__(self):
        self.name = ''
        self.image = None
        self.events = []

    def _displayLocationScreen(self, currentEvents):

        cfg.DISPLAYSURF.blit(self.image, (0,0))

        x = 40
        y = 50
        for i in currentEvents:
            eventBackSurf = pygame.Surface((320, 76))
            eventBackSurf.set_alpha(140)
            eventBackSurf.fill(cfg.BLACK)
            eventBackRect = eventBackSurf.get_rect()
            eventBackRect.topleft = (x, y)

            eventImageSurf = pygame.transform.scale(i.image, (72, 72))
            eventImageRect = eventImageSurf.get_rect()
            eventImageRect.topleft = (eventBackRect.left + 2, eventBackRect.top + 2)

            eventNameSurf = cfg.BASICFONT.render(i.displayName, True, cfg.WHITE)
            eventNameRect = eventNameSurf.get_rect()
            eventNameRect.midleft = (eventImageRect.right + 15, eventBackRect.centery)

            if eventBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                eventBackSurf.fill(cfg.BLUE)
                eventBackSurf.set_alpha(100)
                eventNameSurf = cfg.BASICFONT.render(i.displayName, True, cfg.RED)
                if cfg.mouseClicked:
                    return i

            cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 1)
            cfg.DISPLAYSURF.blit(eventImageSurf, eventImageRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventImageRect, 1)
            cfg.DISPLAYSURF.blit(eventNameSurf, eventNameRect)

            y += 80

        leaveBackSurf = pygame.Surface((150, 50))
        leaveBackSurf.set_alpha(140)
        leaveBackSurf.fill(cfg.BLACK)
        leaveBackRect = leaveBackSurf.get_rect()
        leaveBackRect.bottomright = (cfg.WINWIDTH - 15, cfg.WINHEIGHT - 10)
        leaveSurf = cfg.BASICFONT.render('Leave', True, cfg.WHITE)
        leaveRect = leaveSurf.get_rect()
        leaveRect.center = leaveBackRect.center
        if leaveBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
            leaveSurf = cfg.BASICFONT.render('Leave', True, cfg.RED)
            if cfg.mouseClicked:
                return 'Leave'
        cfg.DISPLAYSURF.blit(leaveBackSurf, leaveBackRect)
        cfg.DISPLAYSURF.blit(leaveSurf, leaveRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, leaveBackRect, 2)

    def _locationBackground(self):

        maskSurf = pygame.Surface((cfg.WINWIDTH, cfg.WINHEIGHT))
        maskSurf.fill(cfg.BLACK)
        maskSurf.set_alpha(100)

        cfg.DISPLAYSURF.blit(self.image, (0,0))
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))

""" ------------------------------------------------------------------------ """
