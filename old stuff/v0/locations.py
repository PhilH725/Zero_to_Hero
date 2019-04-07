
""" location class for zth
      locations are areas within hubs that can be explored. they contain events. """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class Location():
    def __init__(self):
        self.name = ''
        self.hub = ''
        self.image = None
        self.events = []

    def _displayLocationScreen(self):

        cfg.DISPLAYSURF.blit(self.image, (0,0))

        x = 40
        y = 50
        for i in self.events:
            eventBackSurf = pygame.Surface((320, 76))
            eventBackSurf.set_alpha(140)
            eventBackSurf.fill(cfg.BLACK)
            eventBackRect = eventBackSurf.get_rect()
            eventBackRect.topleft = (x, y)

            eventImageSurf = pygame.transform.scale(i.image, (72, 72))
            eventImageRect = eventImageSurf.get_rect()
            eventImageRect.topleft = (eventBackRect.left + 2, eventBackRect.top + 2)

            eventNameSurf = cfg.BASICFONT.render(i.name, True, cfg.WHITE)
            eventNameRect = eventNameSurf.get_rect()
            eventNameRect.midleft = (eventImageRect.right + 15, eventBackRect.centery)

            if eventBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                eventBackSurf.fill(cfg.BLUE)
                eventBackSurf.set_alpha(100)
                eventNameSurf = cfg.BASICFONT.render(i.name, True, cfg.RED)
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
        leaveBackRect.bottomleft = (50, cfg.WINHEIGHT - 50)
        leaveSurf = cfg.BASICFONT.render('Leave', True, cfg.WHITE)
        leaveRect = leaveSurf.get_rect()
        leaveRect.center = leaveBackRect.center
        if leaveBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
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



""" ---------------------------- """

rwInn = Location()
rwInn.name = 'Riverwood Inn'
rwInn.hub = 'Riverwood'
rwInn.image = pygame.image.load('images/bg/inn-small.bmp')

rwTavern = Location()
rwTavern.name = 'Riverwood Tavern'
rwTavern.hub = 'Riverwood'
rwTavern.image = pygame.image.load('images/bg/tavern.png')

rwFarm = Location()
rwFarm.name = 'Riverwood Farmhouse'
rwFarm.hub = 'Riverwood'
rwFarm.image = pygame.image.load('images/bg/farmhouse.bmp')

LOCLIST = [rwInn, rwTavern, rwFarm]

""" ------------------------------------------------------------------------ """
