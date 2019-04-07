
""" class functions for zth
      this is gonna be a giant file, but i dont like everything being so spread out. """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

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

""" ---------------------------------- """
#player class

class Player():
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('images/avi/phil.png')
        self.playerClass = 'Warrior'

        self.classStats = {}

        self.stats = {
            'Health': 50 ,
            'Strength': 50 ,
            'Endurance': 50 ,

            'Intelligence': 50 ,
            'Perception': 50 ,
            'Focus': 50 ,

            'Charisma': 50 ,
            'Stealth': 50 ,
            'Speed': 50
        }

        self.coords = (380, 280) #current location of the player. will match with a hub or be in the wilderness

""" ------------------------------------------------------------------------ """
#hub class

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
# event class

class Event():
    """ main event class. contains variables present in all children classes and some basic display functions. """
    def __init__(self):
        self.tag = '' #also known as eventName, this is used to directly select the event and should be unique
        self.displayName = '' #name that appears on location screen when selecting an npc
        self.charName = '' #name that appears under the avatar in the textbox
        self.image = None #avatar image
        self.reqs = {} #requirements for the event to be active. should be a PROGRESSIONDICT key and a list of int values that apply
                        #left empty is no requirements. 'NaN':9 is the placeholder for an event that cant have reqs met.
        self.progression = {} #changes PROGRESSIONDICT key to the val number upon event completion

        self.eventBackRect = pygame.Rect(120, 20, 650, 250) #display aid

    def _drawEventTextBox(self):

        #draws the main text box
        eventBackSurf = pygame.Surface((650, 250))
        eventBackSurf.fill(cfg.BLUE)
        eventBackSurf.set_alpha(160)
        eventBackRect = eventBackSurf.get_rect()
        eventBackRect.topleft = (120, 20)
        cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 2)

        #line to separate the very bottom of the box to make it clearer that choices are below
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (eventBackRect.left + 5, eventBackRect.bottom - 32),
            (eventBackRect.right - 5, eventBackRect.bottom - 32), 1)

        #if the event has an image it is displayed to the left of the textbox
        if self.image:
            aviBackSurf = pygame.Surface((96,96))
            aviBackSurf.set_alpha(170)
            aviBackRect = aviBackSurf.get_rect()
            aviBackRect.bottomright = (eventBackRect.left - 10, eventBackRect.centery)
            aviSurf = self.image
            aviRect = aviSurf.get_rect()
            aviRect.bottomright = (eventBackRect.left - 10, eventBackRect.centery)

            cfg.DISPLAYSURF.blit(aviBackSurf, aviBackRect)
            cfg.DISPLAYSURF.blit(aviSurf, aviRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, aviRect, 2)

        if self.charName:
            nameBackSurf = pygame.Surface((100, 20))
            nameBackSurf.set_alpha(170)
            nameBackRect = nameBackSurf.get_rect()
            nameBackRect.topright = (eventBackRect.left - 7, eventBackRect.centery + 2)
            nameSurf = cfg.AR17.render(self.charName, True, cfg.WHITE)
            nameRect = nameSurf.get_rect()
            nameRect.center = nameBackRect.center
            cfg.DISPLAYSURF.blit(nameBackSurf, nameBackRect)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, nameBackRect, 1)

""" ---------------------------- """

class TextEvent(Event):
    """simple events that display text in a list of lists, where each list is a page of dialogue.
        they are completed upon advancing past the last page of dialogue. """

    def __init__(self):
        super().__init__()

        self.type = 'Text'
        self.text = [[]]

    def _playTextEvent(self, player):

        eventPos = 0 #tells the function which page of dialogue to read
        while True:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            #basic text display function. reads one list at a time
            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            if eventPos > len(self.text) - 2:
                conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
                conRect = conSurf.get_rect()
                conRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if conRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    conSurf = cfg.BASICFONT.render('Continue', True, cfg.RED)
                    if cfg.mouseClicked:
                        if self.progression:
                            for i, v in self.progression.items():
                                cfg.PROGRESSIONDICT[i] = v
                        return
                cfg.DISPLAYSURF.blit(conSurf, conRect)
            else:
                nextSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
                nextRect = nextSurf.get_rect()
                nextRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if nextRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    nextSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                    if cfg.mouseClicked:
                        eventPos += 1
                cfg.DISPLAYSURF.blit(nextSurf, nextRect)

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class ComplexEvent(Event):
    """events that lead into a choice, with variable handling options from there. """

    def __init__(self):
        super().__init__()

        self.type = 'Complex'
        self.tag = ''
        self.text = [[]]
        self.choices = {} #keys are the choices that appear, vals are the tag for the event to be played directly after the choice
                        #note that 'Done' should be the val for a choice that ends the conversation and does nothing.

    def _playComplexEvent(self, player):

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            #same text display function
            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            x = self.eventBackRect.right - 20
            y = self.eventBackRect.bottom - 5
            if eventPos == len(self.text) - 1:
                for i in list(self.choices)[::-1]:
                    choiceSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                    choiceRect = choiceSurf.get_rect()
                    choiceRect.bottomright = (x, y)
                    if choiceRect.collidepoint(cfg.mouseX, cfg.mouseY):
                        choiceSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                        if cfg.mouseClicked:
                            return self.choices[i]
                    cfg.DISPLAYSURF.blit(choiceSurf, choiceRect)
                    x -= 100

            else:
                nextSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
                nextRect = nextSurf.get_rect()
                nextRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if nextRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    nextSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                    if cfg.mouseClicked:
                        eventPos += 1
                cfg.DISPLAYSURF.blit(nextSurf, nextRect)

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class ContinuationEvent(Event):
    """ niche event that simplifies events that happen after a choice. """
    #used only for follow up simple text events, not more complex events

    def __init__(self):
        super().__init__()

        self.type = 'Continuation'
        self.parent = ''
        self.tag = ''
        self.textOne = []
        self.textTwo = []
        self.textThree = []
        self.progOne = {}
        self.progTwo = {}
        self.progThree = {}

    def _playContinuationEvent(self, player, choice):

        if choice == '1':
            text = self.textOne
            prog = self.progOne
        elif choice == '2':
            text = self.textTwo
            prog = self.progTwo
        elif choice == '3':
            text = self.textThree
            prog = self.progThree

        self.name = cfg.activeComplexEvent.name
        self.image = cfg.activeComplexEvent.image

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            if eventPos > len(text) - 2:
                conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
                conRect = conSurf.get_rect()
                conRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if conRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    conSurf = cfg.BASICFONT.render('Continue', True, cfg.RED)
                    if cfg.mouseClicked:
                        if prog:
                            for i, v in prog.items():
                                cfg.PROGRESSIONDICT[i] = v
                        return
                cfg.DISPLAYSURF.blit(conSurf, conRect)
            else:
                nextSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
                nextRect = nextSurf.get_rect()
                nextRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if nextRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    nextSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                    if cfg.mouseClicked:
                        eventPos += 1
                cfg.DISPLAYSURF.blit(nextSurf, nextRect)

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class MissionEvent(Event):
    def __init__(self):
        super().__init__()

        self.type = 'Mission'
        self.actions = ['Yes', 'No']



    def _playMissionEvent(self, player):

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            #same text display function
            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            x = self.eventBackRect.right - 20
            y = self.eventBackRect.bottom - 5
            if eventPos == len(self.text) - 1:
                for i in self.choices[::-1]:
                    choiceSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                    choiceRect = choiceSurf.get_rect()
                    choiceRect.bottomright = (x, y)
                    if choiceRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                        choiceSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                        if cfg.mouseClicked:
                            return i
                    cfg.DISPLAYSURF.blit(choiceSurf, choiceRect)
                    x -= 100

            else:
                nextSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
                nextRect = nextSurf.get_rect()
                nextRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
                if nextRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    nextSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                    if cfg.mouseClicked:
                        eventPos += 1
                cfg.DISPLAYSURF.blit(nextSurf, nextRect)

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class ShopEvent(Event):

    def __init__(self):
        super().__init__()

        self.type = 'Shop'
        self.displayName = 'Shopkeeper'
        self.charName = 'Shopkeeper'
        self.image = pygame.image.load('images/avi/shopkeeper.png')
        self.text = [
            "Looking to buy something?"
        ]
        self.stock = {}

    def _playShopEvent(self, player):

        action = None
        while not action:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            shopSurf = cfg.BASICFONT.render('Shop', True, cfg.WHITE)
            shopRect = shopSurf.get_rect()
            shopRect.bottomright = (self.eventBackRect.right - 45, self.eventBackRect.bottom - 5)
            if shopRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                shopSurf = cfg.BASICFONT.render('Shop', True, cfg.RED)
                if cfg.mouseClicked:
                    action = 'Shop'
            cfg.DISPLAYSURF.blit(shopSurf, shopRect)

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

        self._shopProcessing(player)
        return

    def _shopProcessing(self, player):

        while True:

            common_functions.standardEventHandling()

            player._focusForeground()

            item = self._drawShopBox()


            if item:
                if item == 'Exit':
                    return
                else:
                    pass #will do more with this when items are more of a thing. no reason to chart this out before items are done.

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

    def _drawShopBox(self):

        shopBackSurf = pygame.Surface((600, 400))
        shopBackSurf.fill(cfg.BLUE)
        shopBackSurf.set_alpha(200)
        shopBackRect = shopBackSurf.get_rect()
        shopBackRect.topleft = (100, 75)

        cfg.DISPLAYSURF.blit(shopBackSurf, shopBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, shopBackRect, 2)

        x = shopBackRect.left + 10
        y = shopBackRect.top + 10
        for i, v in self.stock.items():
            itemSurf = cfg.AR19.render(i, True, cfg.WHITE)
            itemRect = itemSurf.get_rect()
            itemRect.topleft = (x, y)
            costSurf = cfg.AR19.render(str(v), True, cfg.WHITE)
            costRect = costSurf.get_rect()
            costRect.topright = (shopBackRect.centerx - 10, y)
            highlightRect = pygame.Rect(shopBackRect.left, y, shopBackRect.width / 2, 28)
            if highlightRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                itemSurf = cfg.AR19.render(i, True, cfg.RED)
                costSurf = cfg.AR19.render(str(v), True, cfg.RED)
                if cfg.mouseClicked:
                    return i
            cfg.DISPLAYSURF.blit(itemSurf, itemRect)
            cfg.DISPLAYSURF.blit(costSurf, costRect)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (shopBackRect.left + 5, y + 22), (shopBackRect.right - 5, y + 22), 1)
            y += 28
        shopDividerLength = (28 * len(list(self.stock))) - 4
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (shopBackRect.centerx - 60, shopBackRect.top + 5),
            (shopBackRect.centerx - 60, (shopBackRect.top + 2) + shopDividerLength), 1)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (shopBackRect.centerx, shopBackRect.top + 5),
            (shopBackRect.centerx, shopBackRect.bottom - 5), 1)

        exitSurf = cfg.AR19.render('Exit', True, cfg.WHITE)
        exitRect = exitSurf.get_rect()
        exitRect.bottomright = (shopBackRect.right - 10, shopBackRect.bottom - 5)
        if exitRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
            exitSurf = cfg.AR19.render('Exit', True, cfg.RED)
            if cfg.mouseClicked:
                return 'Exit'
        cfg.DISPLAYSURF.blit(exitSurf, exitRect)

""" ---------------------------- """

class InnEvent(Event):
    """ simple but unique event where you pay a set amount of gold to rest for a night """

    def __init__(self):
        super().__init__()

        self.type = 'Inn'
        self.text = [
            "Do you want to stay at the inn?" ,
            "The price is 10 gold."
        ]
        self.price = 10 #default values, these can be changed
        self.actions = ['Yes', 'No']

    def _playInnEvent(self, player):

        #waits for you to choose yes or no
        action = None
        while not action:

            common_functions.standardEventHandling()

            player._focusForeground()

            self._drawEventTextBox()

            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            x = self.eventBackRect.right - 45
            y = self.eventBackRect.bottom - 5
            for i in self.actions[::-1]:
                actionSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                actionRect = actionSurf.get_rect()
                actionRect.bottomright = (x, y)
                if actionRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    actionSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                    if cfg.mouseClicked:
                        action = i
                cfg.DISPLAYSURF.blit(actionSurf, actionRect)
                x -= 120

            player._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

        if action == 'Yes':
            self._processInn(player)

        return

    def _processInn(self, player):

        maskSurf = pygame.Surface((cfg.WINWIDTH, cfg.WINHEIGHT))
        maskSurf.fill(cfg.BLACK)
        maskSurf.set_alpha()

        cfg.SOUNDDICT['Inn'].play()
        #plays the inn music and fades the screen out
        for i in range(0,256,2):
            maskSurf.set_alpha(i)
            cfg.DISPLAYSURF.blit(maskSurf, (0,0))

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

        cfg.SOUNDDICT['Morning'].play()
        #proper amount of gold is charged and one day is advanced.
        player.gold -= self.price
        player.day += 1
        player.time = 8.5

""" ----------------------------------- """

class JobEvent(Event):

    def __init__(self):
        super().__init__()

        self.type = 'Special'
        self.typeTwo = ''
        self.availableJobs = []

    def _displayJobBoard(self, game):

        jobPreview = None
        jobIndex = 0
        while True:

            common_functions.standardEventHandling()

            game._focusForeground()

            action = self.availableJobs[jobIndex]._jobPosting()

            if action == 'Take Job':
                game.activeJobs.append(self.availableJobs[jobIndex])
                return
            elif action == 'Stop Looking':
                return

            nextSurf = cfg.IMAGEDICT['Right One']
            nextRect = nextSurf.get_rect()
            nextRect.midright = (cfg.WINWIDTH - 20, cfg.WINHEIGHT / 2)
            if nextRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                nextSurf = cfg.IMAGEDICT['Right Two']
                if cfg.mouseClicked:
                    jobIndex += 1
                    if jobIndex > len(self.availableJobs) - 1:
                        jobIndex = 0
            cfg.DISPLAYSURF.blit(nextSurf, nextRect)

            game._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

    def _drawAvailableJobs(self):

        x = 100
        y = 20
        for i in self.availableJobs:
            jobBackSurf = pygame.Surface((600,80))
            jobBackSurf.set_alpha(115)
            jobBackSurf.fill(cfg.BLUE)
            jobBackRect = jobBackSurf.get_rect()
            jobBackRect.topleft = (x, y)

            jobNameSurf = cfg.BASICFONT.render(i.jobName, True, cfg.WHITE)
            jobNameRect = jobNameSurf.get_rect()
            jobNameRect.midleft = (jobBackRect.left + 15, jobBackRect.centery)

            if jobBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
                jobBackSurf.set_alpha(200)
                jobNameSurf = cfg.BASICFONT.render(i.jobName, True, cfg.RED)
                if cfg.mouseClicked:
                    return i

            cfg.DISPLAYSURF.blit(jobBackSurf, jobBackRect)
            cfg.DISPLAYSURF.blit(jobNameSurf, jobNameRect)

            y += 85

""" ------------------------------------------------------------------------ """
# job class

class Job():
    def __init__(self, jobName):
        self.jobName = jobName
        self.description = []
        self.reqs = {}
        self.distance = 0
        self.rewards = {}

    def _jobPosting(self):

        jobBackSurf = pygame.Surface((650, 480))
        jobBackSurf.fill(cfg.BLUE)
        jobBackSurf.set_alpha(180)
        jobBackRect = jobBackSurf.get_rect()
        jobBackRect.topleft = (75,10)
        cfg.DISPLAYSURF.blit(jobBackSurf, jobBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, jobBackRect, 2)

        jobTitleSurf = cfg.AR21.render(self.jobName, True, cfg.WHITE)
        jobTitleRect = jobTitleSurf.get_rect()
        jobTitleRect.midtop = (jobBackRect.centerx, jobBackRect.top + 5)
        cfg.DISPLAYSURF.blit(jobTitleSurf, jobTitleRect)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobBackRect.left + 5, jobTitleRect.bottom + 5),
            (jobBackRect.right - 5, jobTitleRect.bottom + 5), 2)

        acceptBackSurf = pygame.Surface((180, 50))
        acceptBackSurf.fill(cfg.GREEN)
        acceptBackSurf.set_alpha(80)
        acceptBackRect = acceptBackSurf.get_rect()
        acceptBackRect.topleft = (jobBackRect.left + 50, jobBackRect.bottom + 8)
        acceptSurf = cfg.AR25.render('Take Job', True, cfg.WHITE)
        acceptRect = acceptSurf.get_rect()
        acceptRect.center = acceptBackRect.center

        denyBackSurf = pygame.Surface((180, 50))
        denyBackSurf.fill(cfg.RED)
        denyBackSurf.set_alpha(80)
        denyBackRect = denyBackSurf.get_rect()
        denyBackRect.topright = (jobBackRect.right - 50, jobBackRect.bottom + 8)
        denySurf = cfg.AR25.render('Stop Looking', True, cfg.WHITE)
        denyRect = denySurf.get_rect()
        denyRect.center = denyBackRect.center

        if acceptBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            acceptBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Take Job'

        if denyBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            denyBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Stop Looking'

        cfg.DISPLAYSURF.blit(acceptBackSurf, acceptBackRect)
        cfg.DISPLAYSURF.blit(acceptSurf, acceptRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, acceptBackRect, 2)
        cfg.DISPLAYSURF.blit(denyBackSurf, denyBackRect)
        cfg.DISPLAYSURF.blit(denySurf, denyRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, denyBackRect, 2)







    def _viewJobDetails(self):

        backSurf = pygame.Surface((650, 480))
        backSurf.fill(cfg.BLUE)
        backSurf.set_alpha(180)
        backRect = backSurf.get_rect()
        backRect.topleft = (75,10)

        titleSurf = cfg.AR25.render(self.jobName, True, cfg.WHITE)
        titleRect = titleSurf.get_rect()
        titleRect.midtop = (backRect.centerx, backRect.top + 5)

        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        cfg.DISPLAYSURF.blit(titleSurf, titleRect)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, titleRect.bottom + 5), (backRect.right - 5, titleRect.bottom + 5), 2)

        x = backRect.left + 10
        y = titleRect.bottom + 15
        for i in self.description:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 35

        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, backRect.centery), (backRect.right - 5, backRect.centery), 2)

        skillReqSurf = cfg.AR19.render('Skill Recommendations: ', True, cfg.WHITE)
        skillReqRect = skillReqSurf.get_rect()
        skillReqRect.topleft = (backRect.left + 10, backRect.centery + 5)
        cfg.DISPLAYSURF.blit(skillReqSurf, skillReqRect)

        x = backRect.left + 5
        y = skillReqRect.bottom + 5
        for i, v in self.reqs.items():
            skillSurf = cfg.AR19.render('-%s: %s' % (i, v), True, cfg.WHITE)
            skillRect = skillSurf.get_rect()
            skillRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(skillSurf, skillRect)
            y += 28

        rewardHeaderSurf = cfg.AR19.render('Reward: ', True, cfg.WHITE)
        rewardHeaderRect = rewardHeaderSurf.get_rect()
        rewardHeaderRect.topright = (backRect.right - 50, backRect.centery + 5)
        cfg.DISPLAYSURF.blit(rewardHeaderSurf, rewardHeaderRect)

        x = backRect.right - 150
        y = rewardHeaderRect.bottom + 5
        for i, v in self.rewards.items():
            rewardSurf = cfg.AR19.render('-%s: %s' % (i, v), True, cfg.WHITE)
            rewardRect = rewardSurf.get_rect()
            rewardRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(rewardSurf, rewardRect)
            y += 28

        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, backRect.bottom - 50), (backRect.right - 5, backRect.bottom - 50), 2)

        travelHeaderSurf = cfg.AR19.render('Travel Time (Days/One Way): ', True, cfg.WHITE)
        travelHeaderRect = travelHeaderSurf.get_rect()
        travelHeaderRect.bottomleft = (backRect.left + 25, backRect.bottom - 10)
        travelSurf = cfg.AR19.render('%s' % self.distance, True, cfg.WHITE)
        travelRect = travelSurf.get_rect()
        travelRect.bottomleft = (travelHeaderRect.right + 5, backRect.bottom - 10)
        cfg.DISPLAYSURF.blit(travelHeaderSurf, travelHeaderRect)
        cfg.DISPLAYSURF.blit(travelSurf, travelRect)

        acceptBackSurf = pygame.Surface((200, 65))
        acceptBackSurf.fill(cfg.GREEN)
        acceptBackSurf.set_alpha(80)
        acceptBackRect = acceptBackSurf.get_rect()
        acceptBackRect.topleft = (backRect.left + 50, backRect.bottom + 10)
        acceptSurf = cfg.AR25.render('Take Job', True, cfg.WHITE)
        acceptRect = acceptSurf.get_rect()
        acceptRect.center = acceptBackRect.center

        denyBackSurf = pygame.Surface((200, 65))
        denyBackSurf.fill(cfg.RED)
        denyBackSurf.set_alpha(80)
        denyBackRect = denyBackSurf.get_rect()
        denyBackRect.topright = (backRect.right - 50, backRect.bottom + 10)
        denySurf = cfg.AR25.render('Keep Looking', True, cfg.WHITE)
        denyRect = denySurf.get_rect()
        denyRect.center = denyBackRect.center

        if acceptBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            acceptBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Take Job'

        if denyBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            denyBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Keep Looking'

        cfg.DISPLAYSURF.blit(acceptBackSurf, acceptBackRect)
        cfg.DISPLAYSURF.blit(acceptSurf, acceptRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, acceptBackRect, 2)
        cfg.DISPLAYSURF.blit(denyBackSurf, denyBackRect)
        cfg.DISPLAYSURF.blit(denySurf, denyRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, denyBackRect, 2)

""" --------------------------------- """
#















#
