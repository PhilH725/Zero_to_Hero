
""" contains the player class, which contains all of the main gameplay variables
        i might split things up later, but for now this encapsulates most things """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class Player():
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('images/avi/phil.png')
        """self.stats = { #ill make stats customizable later, theyre just on phil defaults for now
            'Power': 50 , #power is overall fighting abilitiy, regardless of details. warrior/mage/hiring bodyguards, etc
            'Condition': 25 , #physical condition, affects carrying capacity, travel speed, disease resist, etc
            'Perception': 40 , #affects combat ability, ability to find things
            'Charisma': 25 , #talk skill
            'Intelligence': 70 #dont know what all this affects yet
        }"""
        self.playerClass = 'Warrior'

        self.stats = {
            'Primary Weapon': 50 ,
            'Secondary Weapon': 50 ,
            'Defense': 50 ,

            'Health': 50 ,
            'Strength': 50 ,
            'Endurance': 50 ,

            'Intelligence': 50 ,
            'Perception': 50 ,
            'Mental3': 50 ,

            'Charisma': 50 ,
            'Street Skills': 50 ,
            'Stealth': 50
        }

        self.coords = (420, 315) #current location of the player. will match with a hub or be in the wilderness
        self.bgImage = '' #used to display backgrounds during events and other things where only player class is given

        self.inventory = {'Food Ration': 5, 'Iron Sword': 1, 'Antidote': 1}
        self.activeJobs = []

        #gamestate stuff, im keeping it here for now but am open to moving it
        self.day = 1
        self.gold = 1000
        self.time = 8.5

    def _displayHud(self):

        imageBackSurf = pygame.Surface((100, 100))
        imageBackSurf.fill(cfg.BLACK)
        imageBackSurf.set_alpha(180)
        imageBackRect = imageBackSurf.get_rect()
        imageBackRect.bottomleft = (0, cfg.WINHEIGHT)
        imageSurf = self.image
        imageRect = imageSurf.get_rect()
        imageRect.bottomleft = (2, cfg.WINHEIGHT - 2)

        cfg.DISPLAYSURF.blit(imageBackSurf, imageBackRect)
        cfg.DISPLAYSURF.blit(imageSurf, imageRect)
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
                    if counter == 1:
                        cfg.statDisplayMode = True
                    elif counter == 2:
                        cfg.timeDisplayMode = True
                    elif counter == 3:
                        cfg.goldDisplayMode = True
                    elif counter == 4:
                        cfg.invDisplayMode = True
            cfg.DISPLAYSURF.blit(optionBackSurf, optionBackRect)
            cfg.DISPLAYSURF.blit(optionSurf, optionRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.BLACK, optionBackRect, 1)
            counter += 1
            x += 125

        if cfg.statDisplayMode:
            statDisplayBackSurf = pygame.Surface((400,300))
            statDisplayBackSurf.fill(cfg.BLACK)
            statDisplayBackSurf.set_alpha(220)
            statDisplayBackRect = statDisplayBackSurf.get_rect()
            statDisplayBackRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
            cfg.DISPLAYSURF.blit(statDisplayBackSurf, statDisplayBackRect)

            x = statDisplayBackRect.left + 10
            y = statDisplayBackRect.top + 10
            for i, v in self.stats.items():
                statNameSurf = cfg.BASICFONT.render('%s:' % i, True, cfg.WHITE)
                statNameRect = statNameSurf.get_rect()
                statNameRect.topleft = (x, y)
                statValSurf = cfg.BASICFONT.render(str(v), True, cfg.WHITE)
                statValRect = statValSurf.get_rect()
                statValRect.topright = (statDisplayBackRect.centerx - 20, y)
                cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
                cfg.DISPLAYSURF.blit(statValSurf, statValRect)
                y += 32

        if cfg.invDisplayMode:
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

        if cfg.rightClick:
            cfg.hudMenu = False
            cfg.statDisplayMode = False
            cfg.timeDisplayMode = False
            cfg.goldDisplayMode = False
            cfg.invDisplayMode = False

    def _focusForeground(self):

        maskSurf = pygame.Surface((cfg.WINWIDTH, cfg.WINHEIGHT))
        maskSurf.fill(cfg.BLACK)
        maskSurf.set_alpha(100)

        cfg.DISPLAYSURF.blit(self.bgImage, (0,0))
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))






""" ------------------------------------------------------------------------ """
#probably gonna move this to its own file

class Item():
    def __init__(self, name, weight, type):
        self.name = name
        self.weight = weight
        self.type = type

""" ----------------------------------- """

item1 = Item('Food Ration', 4, 'Item')
item2 = Item('Iron Sword', 20, 'Equip')
item3 = Item('Leather Armor', 8, 'Equip')
item4 = Item('Antidote', .5, 'Item')

ITEMLIST = [item1, item2, item3, item4]








#
