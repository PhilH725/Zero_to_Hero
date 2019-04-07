
""" hubs class for zth
        these are the outermost areas like towns and cities. they contain locations that can be further explored
        and act as a connective area to reach locations within a hub, or in a new one. """
#contains both the Hub class and the code for filling out the main list

import pygame
import cfg, common_functions
import locations

class Hub():
    def __init__(self):
        self.name = ''
        self.image = None
        self.locations = []
        self.coords = (0, 0)

    def _displayHubScreen(self):

        #displays the main background image
        cfg.DISPLAYSURF.blit(self.image, (0,0))

        #displays the title/hub name
        nameBackSurf = pygame.Surface((280, 60))
        nameBackSurf.set_alpha(140)
        nameBackSurf.fill(cfg.BLACK)
        nameBackRect = nameBackSurf.get_rect()
        nameBackRect.midtop = (cfg.WINWIDTH / 2, 10)
        nameSurf = cfg.AR25.render(self.name, True, cfg.WHITE)
        nameRect = nameSurf.get_rect()
        nameRect.center = nameBackRect.center
        cfg.DISPLAYSURF.blit(nameBackSurf, nameBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, nameBackRect, 2)
        cfg.DISPLAYSURF.blit(nameSurf, nameRect)

        #displays all of the hubs possible location destinations. clicking returns the name of the location
        #currently runs off the screen for more than 12, ill deal with that when/if it happens, a lot isnt final yet.
        x = 20
        y = nameBackRect.bottom + 20
        counter = 1
        for i in self.locations:
            locationBackSurf = pygame.Surface((350, 60))
            locationBackSurf.set_alpha(160)
            locationBackSurf.fill(cfg.BLACK)
            locationBackRect = locationBackSurf.get_rect()
            locationBackRect.topleft = (x, y)

            locSurf = cfg.BASICFONT.render(i.name, True, cfg.WHITE)
            locRect = locSurf.get_rect()
            locRect.midleft = (locationBackRect.left + 25, locationBackRect.centery)
            if locationBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                locationBackSurf.fill(cfg.BLUE)
                locationBackSurf.set_alpha(55)
                locSurf = cfg.BASICFONT.render(i.name, True, cfg.RED)
                if cfg.mouseClicked:
                    return i

            cfg.DISPLAYSURF.blit(locationBackSurf, locationBackRect)
            cfg.DISPLAYSURF.blit(locSurf, locRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, locationBackRect, 2)
            y += 65
            counter += 1
            if counter == 7:
                x = (cfg.WINWIDTH / 2) + 20
                y = nameBackRect.bottom + 20

        #option to back out of the hub. will be changed as that function gets thought out.
        leaveBackSurf = pygame.Surface((150, 50))
        leaveBackSurf.set_alpha(140)
        leaveBackSurf.fill(cfg.BLACK)
        leaveBackRect = leaveBackSurf.get_rect()
        leaveBackRect.bottomright = (cfg.WINWIDTH - 15, cfg.WINHEIGHT - 10)
        leaveSurf = cfg.BASICFONT.render('World Map', True, cfg.WHITE)
        leaveRect = leaveSurf.get_rect()
        leaveRect.center = leaveBackRect.center
        if leaveBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            leaveSurf = cfg.BASICFONT.render('World Map', True, cfg.RED)
            if cfg.mouseClicked:
                return 'World Map'
        cfg.DISPLAYSURF.blit(leaveBackSurf, leaveBackRect)
        cfg.DISPLAYSURF.blit(leaveSurf, leaveRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, leaveBackRect, 2)


""" ------------------------------------------------------------------------ """

camp = Hub()
camp.name = 'Camp'
camp.image = pygame.image.load('images/bg/camp-day.bmp')
camp.locations = ['Campfire']
camp.coords = (520, 300)

riverwood = Hub()
riverwood.name = 'Riverwood'
riverwood.image = pygame.image.load('images/bg/riverwood.bmp')
riverwood.locations = [locations.riverwood_inn, locations.riverwood_tavern, locations.riverwood_farm]
riverwood.coords = (420, 315)

astralis = Hub()
astralis.name = 'Astralis HQ'
astralis.image = pygame.image.load('images/bg/astralis.bmp')
astralis.locations = [locations.astralis_main_hall, locations.astralis_gm_office, locations.astralis_training_room,
    locations.astralis_weapon_shop, locations.astralis_hospital, locations.astralis_tavern, locations.astralis_library,
    locations.astralis_homeroom]
astralis.coords = (380, 280)

solitude = Hub()
solitude.name = 'Solitude'
solitude.image = pygame.image.load('images/bg/solitude.bmp')
solitude.locations = ['Shop', 'Inn']
solitude.coords = (75, 75)

daggerfall = Hub()
daggerfall.name = 'Daggerfall'
daggerfall.image = pygame.image.load('images/bg/daggerfall.bmp')
daggerfall.locations = ['Shop', 'Inn']
daggerfall.coords = (65, 520)

cheydinhall = Hub()
cheydinhall.name = 'Cheydinhall'
cheydinhall.image = pygame.image.load('images/bg/cheydinhall.bmp')
cheydinhall.locations = ['Shop', 'Inn']
cheydinhall.coords = (680, 220)

HUBLIST = [camp, riverwood, astralis, solitude, daggerfall, cheydinhall]

""" ------------------------------------------------------------------------ """

#
