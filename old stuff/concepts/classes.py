
""" class functions for sof. """

import pygame
import cfg, common_functions

""" ------------------------------------------------- """

class Player():
    def __init__(self, name):
        self.name = name
        self.stats = {'Power': 50 , 'Strength': 25 , 'Perception': 40 , 'Endurance': 20 ,
                        'Charisma': 25 , 'Intelligence': 70}
        #ill make stats customizable later, theyre just on phil defaults for now

        self.gold = 1000
        self.day = 1 #this prob belongs in a game state object, but its the only thing for now so just putting it here.

    def _displayPlayerStats(self):
        #ugly concept version. the real version is the same idea just prettier

        #this just lets me display three letter abbrevs instead of the whole stat name
        displayStats = ['Pow: %s' % self.stats['Power'], 'Str: %s' % self.stats['Strength'], 'Per: %s' % self.stats['Perception'],
                    'End: %s' % self.stats['Endurance'], 'Chr: %s' % self.stats['Charisma'], 'Int: %s' % self.stats['Intelligence']]

        gameState = ['Day: %s' % self.day, 'Gold: %s' % self.gold]

        x = 15
        y = cfg.WINHEIGHT - 10
        for i in gameState:
            stateSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            stateRect = stateSurf.get_rect()
            stateRect.bottomleft = (x, y)
            cfg.DISPLAYSURF.blit(stateSurf, stateRect)
            x += 90

        x = cfg.WINWIDTH - 15
        y = cfg.WINHEIGHT - 10
        for i in displayStats[::-1]:
            statSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            statRect = statSurf.get_rect()
            statRect.bottomright = (x, y)
            cfg.DISPLAYSURF.blit(statSurf, statRect)
            x -= 80


""" ------------------------------------------------------------------------ """

class Hub():
    def __init__(self):
        self.name = ''
        self.image = None
        self.locations = []

    def _displayHubScreen(self):

        cfg.DISPLAYSURF.blit(self.image, (0,0))

        nameBackSurf = pygame.Surface((280, 60))
        nameBackSurf.set_alpha(140)
        nameBackSurf.fill(cfg.BLACK)
        nameBackRect = nameBackSurf.get_rect()
        nameBackRect.midtop = (cfg.WINWIDTH / 2, 5)
        nameSurf = cfg.AR25.render(self.name, True, cfg.WHITE)
        nameRect = nameSurf.get_rect()
        nameRect.center = nameBackRect.center
        cfg.DISPLAYSURF.blit(nameBackSurf, nameBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, nameBackRect, 2)
        cfg.DISPLAYSURF.blit(nameSurf, nameRect)

        if len(self.locations) > 8:
            backWidth = 450
            backHeight = 400
        else:
            backWidth = 220
            backHeight = len(self.locations) * 50

        locationBackSurf = pygame.Surface((backWidth, backHeight))
        locationBackSurf.set_alpha(160)
        locationBackSurf.fill(cfg.BLACK)
        locationBackRect = locationBackSurf.get_rect()
        locationBackRect.topleft = (20, nameBackRect.bottom + 20)
        cfg.DISPLAYSURF.blit(locationBackSurf, locationBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, locationBackRect, 2)

        x = locationBackRect.left + 35
        y = locationBackRect.top + 10
        for i in self.locations:
            locSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            locRect = locSurf.get_rect()
            locRect.topleft = (x, y)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (locationBackRect.left + 3, y + 28), (locationBackRect.right - 3, y + 28), 2)
            if locRect.collidepoint(cfg.mouseX, cfg.mouseY):
                locSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                if cfg.mouseClicked:
                    return i
            cfg.DISPLAYSURF.blit(locSurf, locRect)
            y += 50

        leaveBackSurf = pygame.Surface((150, 50))
        leaveBackSurf.set_alpha(140)
        leaveBackSurf.fill(cfg.BLACK)
        leaveBackRect = leaveBackSurf.get_rect()
        leaveBackRect.bottomright = (cfg.WINWIDTH - 50, cfg.WINHEIGHT - 50)
        leaveSurf = cfg.BASICFONT.render('Leave Hub', True, cfg.WHITE)
        leaveRect = leaveSurf.get_rect()
        leaveRect.center = leaveBackRect.center
        if leaveBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            leaveSurf = cfg.BASICFONT.render('Leave Hub', True, cfg.RED)
            if cfg.mouseClicked:
                return 'Leave'
        cfg.DISPLAYSURF.blit(leaveBackSurf, leaveBackRect)
        cfg.DISPLAYSURF.blit(leaveSurf, leaveRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, leaveBackRect, 2)

""" ----------------------------------- """

camp = Hub()
camp.name = 'Camp'
camp.image = pygame.image.load('images/bg/camp.bmp')
camp.locations = ['Campfire']

riverwood = Hub()
riverwood. name = 'Riverwood'
riverwood.image = pygame.image.load('images/bg/riverwood.bmp')
riverwood.locations = ['Riverwood Inn', 'Riverwood Tavern', 'Riverwood Farmhouse']

hubList = [camp, riverwood]

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

            if eventBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
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

locationList = [rwInn, rwTavern, rwFarm]

""" ------------------------------------------------------------------------ """

class Event():
    def __init__(self):
        self.name = ''
        self.location = ''
        self.image = None
        self.tag = ''
        self.reqs = {}
        self.progression = {}

        self.eventBackRect = pygame.Rect(120, 20, 650, 250)

    def _drawEventTextBox(self):

        eventBackSurf = pygame.Surface((650, 250))
        eventBackSurf.fill(cfg.BLUE)
        eventBackSurf.set_alpha(160)
        eventBackRect = eventBackSurf.get_rect()
        eventBackRect.topleft = (120, 20)
        cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 2)

        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (eventBackRect.left + 5, eventBackRect.bottom - 32),
            (eventBackRect.right - 5, eventBackRect.bottom - 32), 1)

        if self.image:
            aviSurf = self.image
            aviRect = aviSurf.get_rect()
            aviRect.bottomright = (eventBackRect.left - 10, eventBackRect.centery)

            cfg.DISPLAYSURF.blit(aviSurf, aviRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, aviRect, 2)

""" ---------------------------- """

class TextEvent(Event):
    def __init__(self):
        super().__init__()

        self.type = 'Text'
        self.text = [[]]

    def _playTextEvent(self, player, location):

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayPlayerStats()

            self._drawEventTextBox()

            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
            conRect = conSurf.get_rect()
            conRect.bottomright = (self.eventBackRect.right - 5, self.eventBackRect.bottom - 5)
            if conRect.collidepoint(cfg.mouseX, cfg.mouseY):
                conSurf = cfg.BASICFONT.render('Continue', True, cfg.RED)
                if cfg.mouseClicked:
                    eventPos += 1
                    if eventPos > len(self.text) - 1:
                        if self.progression:
                            for i, v in self.progression.items():
                                cfg.PROGRESSIONDICT[i] = v
                        return
            cfg.DISPLAYSURF.blit(conSurf, conRect)

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class ChoiceEvent(Event):
    def __init__(self):
        super().__init__()

        self.type = 'Choice'
        self.text = []
        self.choices = {}

    def _playChoiceEvent(self, player, location):

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayPlayerStats()

            self._drawEventTextBox()

            x = self.eventBackRect.left + 10
            y = self.eventBackRect.top + 10
            for i in self.text[eventPos]:
                lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                lineRect = lineSurf.get_rect()
                lineRect.topleft = (x, y)
                cfg.DISPLAYSURF.blit(lineSurf, lineRect)
                y += 30

            x = self.eventBackRect.right - 5
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
                conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
                conRect = conSurf.get_rect()
                conRect.bottomright = (self.eventBackRect.right - 5, self.eventBackRect.bottom - 5)
                if conRect.collidepoint(cfg.mouseX, cfg.mouseY):
                    conSurf = cfg.BASICFONT.render('Continue', True, cfg.RED)
                    if cfg.mouseClicked:
                        eventPos += 1
                cfg.DISPLAYSURF.blit(conSurf, conRect)

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)



""" ---------------------------- """

class InnEvent(Event):
    def __init__(self):
        super().__init__()

        self.type = 'Inn'
        self.text = [
            "Do you want to stay at the inn?" ,
            "The price is 10 gold."
        ]
        self.price = 10
        self.actions = ['Yes', 'No']

    def _playInnEvent(self, player, location):

        action = None
        while not action:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayPlayerStats()

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
                if actionRect.collidepoint(cfg.mouseX, cfg.mouseY):
                    actionSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                    if cfg.mouseClicked:
                        action = i
                cfg.DISPLAYSURF.blit(actionSurf, actionRect)
                x -= 120

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

        for i in range(0,256,2):
            maskSurf.set_alpha(i)
            cfg.DISPLAYSURF.blit(maskSurf, (0,0))

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

        cfg.SOUNDDICT['Morning'].play()
        player.gold -= self.price
        player.day += 1


""" ---------------------------- """

innkeeper = InnEvent()
innkeeper.name = 'Innkeeper'
innkeeper.location = 'Riverwood Inn'
innkeeper.image = pygame.image.load('images/avi/innkeeper.png')

testNPC = TextEvent()
testNPC.name = 'Guy'
testNPC.location = 'Riverwood Inn'
testNPC.image = pygame.image.load('images/avi/tempguy.png')
testNPC.text = [
    ["Hey, talk about deja vu. Here I am testing simple text events again." ,
    "You'd think it'd be easier to reuse what I've already done, but" ,
    "I kinda think all that is crap and I can make something at least a little" ,
    "more intuitive this time around."] ,
    ["Let's just go onto another page to be sure. This was also a" ,
    "headache the first time around..."]
]

shannon = TextEvent()
shannon.name = 'Shannon'
shannon.location = 'Riverwood Tavern'
shannon.image = pygame.image.load('images/avi/shannon.png')
shannon.text = [
    ["Hey Phil, where the fuck is Zach?" ,
    "He was supposed to be here twenty minutes ago. Go find him."]
]
shannon.progression = {'Shannon Concept': 1}
shannon.reqs = {'Shannon Concept': [0]}

shannonTwo = TextEvent()
shannonTwo.name = 'Shannon'
shannonTwo.location = 'Riverwood Tavern'
shannonTwo.image = pygame.image.load('images/avi/shannon.png')
shannonTwo.text = [
    ["It's about time!"]
]
shannonTwo.reqs = {'Shannon Concept': [2]}

zach = ChoiceEvent()
zach.name = 'Zach'
zach.location = 'Riverwood Farmhouse'
zach.image = pygame.image.load('images/avi/zach.png')
zach.text = [
    ["Hey, how's it going? Shannon? Oh, I know she's waiting," ,
    "I was just hiding out here to piss her off."] ,
    ["You think we should go see her now?"]
]
zach.choices = {'Yes': 'Zach Yes', 'No': 'Zach No'}
zach.reqs = {'Shannon Concept': [1]}

zachYes = TextEvent()
zachYes.name = 'Zach'
zachYes.location = 'Riverwood Farmhouse'
zachYes.image = pygame.image.load('images/avi/zach.png')
zachYes.tag = 'Zach Yes'
zachYes.text = [
    ["Eh, I guess you're right, don't wanna piss her off 'too'",
    "much. Let's go."]
]
zachYes.progression = {'Shannon Concept': 2}
zachYes.reqs = {'NaN': [9]}

zachNo = TextEvent()
zachNo.name = 'Zach'
zachNo.location = 'Riverwood Farmhouse'
zachNo.image = pygame.image.load('images/avi/zach.png')
zachNo.tag = 'Zach No'
zachNo.text = [
    ["Good call, it's so funny fucking with Shannon."] ,
    ["I am just gonna infinite loop until you say yes though," ,
    "so might wanna cut this off eventually."]
]
zachNo.reqs = {'NaN': [9]}

EVENTLIST = [innkeeper, testNPC, shannon, shannonTwo, zach, zachYes, zachNo]











#
