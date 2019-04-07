
""" game state class for zth """

import pygame
import cfg, common_functions
import status_screen

""" ---------------------------------- """
#game class

class Game():
    def __init__(self, player):

        self.player = player #instance of the player class
        self.bgImage = '' #used to display backgrounds during events and other things where only game class is given
        self.time = 8.5
        self.day = 1
        self.inventory = {'Food Ration': 5, 'Iron Sword': 1, 'Antidote': 1}
        self.activeJobs = []
        self.gold = 1000
        self.coords = (380, 280)

        self.statDisplayMode = False
        self.timeDisplayMode = False
        self.goldDisplayMode = False
        self.invDisplayMode = False

    def _displayHud(self):

        self._mainHudMenuBar()

        if cfg.hudMenu:

            if self.statDisplayMode:
                self._statDisplay()
            elif self.timeDisplayMode:
                pass
            elif self.goldDisplayMode:
                pass
            elif self.invDisplayMode:
                self._invDisplay()

    def _mainHudMenuBar(self):

        imageBackSurf = pygame.Surface((100, 100))
        imageBackSurf.fill(cfg.BLACK)
        imageBackSurf.set_alpha(180)
        imageBackRect = imageBackSurf.get_rect()
        imageBackRect.bottomleft = (0, cfg.WINHEIGHT)
        imageSurf = self.player.image
        imageRect = imageSurf.get_rect()
        imageRect.bottomleft = (2, cfg.WINHEIGHT - 2)

        cfg.DISPLAYSURF.blit(imageBackSurf, imageBackRect)
        cfg.DISPLAYSURF.blit(imageSurf, imageRect)

        if imageBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.GREEN, imageRect, 1)
            if cfg.mouseClicked:
                status_screen.statusScreenMenu(self)
        else:
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, imageRect, 1)

        if type(self.time) == int:
            clockTime = '%s:00' % self.time
        else:
            clockTime = '%s:30' % int(self.time)
        hudOptions = ['Stats', 'Time: %s' % clockTime, 'Gold: %s' % self.gold, 'Inventory']

        x = imageBackRect.right + 10
        y = cfg.WINHEIGHT - 5
        counter = 1
        for i in hudOptions:
            optionBackSurf = pygame.Surface((120, 36))
            optionBackSurf.fill(cfg.BEIGE)
            optionBackSurf.set_alpha(180)
            optionBackRect = optionBackSurf.get_rect()
            optionBackRect.bottomleft = (x, y)
            optionSurf = cfg.AR17.render(i, True, cfg.BLACK)
            optionRect = optionSurf.get_rect()
            optionRect.center = optionBackRect.center
            if optionBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
                optionBackSurf.set_alpha(220)
                optionSurf = cfg.AR17.render(i, True, cfg.RED)
                if cfg.mouseClicked:
                    cfg.hudMenu = True
                    self.statDisplayMode = False
                    self.timeDisplayMode = False
                    self.goldDisplayMode = False
                    self.invDisplayMode = False
                    if counter == 1:
                        self.statDisplayMode = True
                    elif counter == 2:
                        self.timeDisplayMode = True
                    elif counter == 3:
                        self.goldDisplayMode = True
                    elif counter == 4:
                        self.invDisplayMode = True
            cfg.DISPLAYSURF.blit(optionBackSurf, optionBackRect)
            cfg.DISPLAYSURF.blit(optionSurf, optionRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.BLACK, optionBackRect, 1)
            counter += 1
            x += 125

        if cfg.rightClick:
            cfg.hudMenu = False
            self.statDisplayMode = False
            self.timeDisplayMode = False
            self.goldDisplayMode = False
            self.invDisplayMode = False

    def _statDisplay(self):

        statDisplayBackSurf = pygame.Surface((500,400))
        statDisplayBackSurf.fill(cfg.BLACK)
        statDisplayBackSurf.set_alpha(220)
        statDisplayBackRect = statDisplayBackSurf.get_rect()
        statDisplayBackRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
        cfg.DISPLAYSURF.blit(statDisplayBackSurf, statDisplayBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, statDisplayBackRect, 2)

        x = statDisplayBackRect.left + 10
        y = statDisplayBackRect.top + 10
        for i, v in self.player.stats.items():
            statNameSurf = cfg.BASICFONT.render('%s:' % i, True, cfg.WHITE)
            statNameRect = statNameSurf.get_rect()
            statNameRect.topleft = (x, y)
            statValSurf = cfg.BASICFONT.render(str(v), True, cfg.WHITE)
            statValRect = statValSurf.get_rect()
            statValRect.topright = (statDisplayBackRect.centerx - 20, y)
            cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
            cfg.DISPLAYSURF.blit(statValSurf, statValRect)
            y += 32

    def _invDisplay(self):

        invBackSurf = pygame.Surface((450, 300))
        invBackSurf.fill(cfg.BLACK)
        invBackSurf.set_alpha(220)
        invBackRect = invBackSurf.get_rect()
        invBackRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
        cfg.DISPLAYSURF.blit(invBackSurf, invBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, invBackRect, 2)

        headerSurf = cfg.BASICFONT.render('Inventory: ', True, cfg.WHITE)
        headerRect = headerSurf.get_rect()
        headerRect.midtop = (invBackRect.centerx, invBackRect.top + 5)
        cfg.DISPLAYSURF.blit(headerSurf, headerRect)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (invBackRect.left + 25, headerRect.bottom + 5),
            (invBackRect.right - 25, headerRect.bottom + 5), 1)

        x = invBackRect.left + 10
        y = headerRect.bottom + 10
        counter = 1
        for i, v in self.inventory.items():
            itemSurf = cfg.AR19.render('%s:' % i, True, cfg.WHITE)
            itemRect = itemSurf.get_rect()
            itemRect.topleft = (x, y)
            amountSurf = cfg.AR19.render(str(v), True, cfg.WHITE)
            amountRect = amountSurf.get_rect()
            amountRect.topright = (invBackRect.centerx - 50, y)
            cfg.DISPLAYSURF.blit(itemSurf, itemRect)
            cfg.DISPLAYSURF.blit(amountSurf, amountRect)
            y += 24
            counter += 1
            if counter > 12:
                pass #will eventually have this make two columns when this gets big enough

    def _missionStatus(self):

        missionBackSurf = pygame.Surface((600, 480))
        missionBackSurf.fill(cfg.BLACK)
        missionBackSurf.set_alpha(220)
        missionBackRect = missionBackSurf.get_rect()
        missionBackRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
        cfg.DISPLAYSURF.blit(missionBackSurf, missionBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, missionBackRect, 2)

    def _focusForeground(self):

        maskSurf = pygame.Surface((cfg.WINWIDTH, cfg.WINHEIGHT))
        maskSurf.fill(cfg.BLACK)
        maskSurf.set_alpha(100)

        cfg.DISPLAYSURF.blit(self.bgImage, (0,0))
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))

""" ------------------------------------------------------------------------ """
