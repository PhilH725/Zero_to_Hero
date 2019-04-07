
""" location class for zth
      locations are areas within hubs that can be explored. they contain events. """

import pygame
import cfg, common_functions
import event_list

""" ------------------------------------------------------------------------ """

class Location():
    def __init__(self):
        self.name = ''
        self.hub = ''
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



""" ---------------------------- """

""" --- """
#astralis

astralis_main_hall = Location()
astralis_main_hall.name = 'Main Hall'
astralis_main_hall.image = pygame.image.load('images/bg/main hall.png')
astralis_main_hall.events = [event_list.job_board]

astralis_gm_office = Location()
astralis_gm_office.name = "Guildmaster's Office"
astralis_gm_office.image = pygame.image.load('images/bg/gm office.bmp')
astralis_gm_office.events = [event_list.amanda_main]

astralis_training_room = Location()
astralis_training_room.name = 'Training Room'
astralis_training_room.image = pygame.image.load('images/bg/training room.bmp')
astralis_training_room.events = []

astralis_weapon_shop = Location()
astralis_weapon_shop.name = 'Guild Weapon Shop'
astralis_weapon_shop.image = pygame.image.load('images/bg/weapon shop.bmp')
astralis_weapon_shop.events = [event_list.astralis_shopkeeper]

astralis_tavern = Location()
astralis_tavern.name = 'Tavern'
astralis_tavern.image = pygame.image.load('images/bg/tavern-big.bmp')
astralis_tavern.events = []

astralis_hospital = Location()
astralis_hospital.name = 'Hospital'
astralis_hospital.image = pygame.image.load('images/bg/hospital.png')
astralis_hospital.events = []

astralis_library = Location()
astralis_library.name = 'Library'
astralis_library.image = pygame.image.load('images/bg/library.png')
astralis_library.events = [event_list.zain_one, event_list.mel_one]

astralis_homeroom = Location()
astralis_homeroom.name = 'Barracks - My Room'
astralis_homeroom.image = pygame.image.load('images/bg/my room.png')
astralis_homeroom.events = [event_list.dorm_bed]

""" --- """
#riverwood

riverwood_inn = Location()
riverwood_inn.name = 'Riverwood Inn'
riverwood_inn.image = pygame.image.load('images/bg/inn-small.bmp')
riverwood_inn.events = [event_list.innkeeper_generic, event_list.riverwood_inn_guy]

riverwood_tavern = Location()
riverwood_tavern.name = 'Riverwood Tavern'
riverwood_tavern.image = pygame.image.load('images/bg/tavern-small.png')
riverwood_tavern.events = [event_list.shannon_intro_one, event_list.shannon_intro_two]

riverwood_farm = Location()
riverwood_farm.name = 'Riverwood Farmhouse'
riverwood_farm.image = pygame.image.load('images/bg/farmhouse.bmp')
riverwood_farm.events = [event_list.zach_intro_one]

""" --- """

LOCLIST = [riverwood_inn, riverwood_tavern, riverwood_farm]

""" ------------------------------------------------------------------------ """
