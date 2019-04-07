
""" event class for zth """

import pygame
import cfg, common_functions

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

class JobContactEvent(Event):
    """ event that activates a job when start reqs are met """
    def __init__(self):
        super().__init__()

        self.type = 'Contact'
        self.text = []

    #pretty sure this just works as a text event. ill keep this here in case i need extra handling later




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

            job = self.availableJobs[jobIndex] #make things easier to read
            action = job._jobPosting()

            if action == 'Take Job':
                job.startDay = game.day
                job.dueDay = job.startDay + job.allowedTime
                game.activeJobs.append(job)
                cfg.PROGRESSIONDICT[job.jobName] = 0
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
