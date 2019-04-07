
""" event class for zth
      events are any number of things from dialogue boxes to game progression. there are different
      child classes for each event type. """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class Event():
    """ main event class. contains variables present in all children classes and some basic display functions. """
    def __init__(self):
        self.tag = '' #also known as eventName, this is used to directly select the event and should be unique
        self.name = '' #charName. name displayed if the character is speaking
        self.location = '' #location the event occurs in. as of now, can only be one location and should be unique to prevent bugs
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
            aviSurf = self.image
            aviRect = aviSurf.get_rect()
            aviRect.bottomright = (eventBackRect.left - 10, eventBackRect.centery)

            cfg.DISPLAYSURF.blit(aviSurf, aviRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, aviRect, 2)

""" ---------------------------- """

class TextEvent(Event):
    """simple events that display text in a list of lists, where each list is a page of dialogue.
        they are completed upon advancing past the last page of dialogue. """

    def __init__(self):
        super().__init__()

        self.type = 'Text'
        self.text = [[]]

    def _playTextEvent(self, player, location):

        eventPos = 0 #tells the function which page of dialogue to read
        while True:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayHud()

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

            #the only option is to continue advancing through the text
            #progression is updated before returning because events can be accessed in different ways
            conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
            conRect = conSurf.get_rect()
            conRect.bottomright = (self.eventBackRect.right - 20, self.eventBackRect.bottom - 5)
            if conRect.collidepoint(cfg.mouseX, cfg.mouseY):
                conSurf = cfg.BASICFONT.render('Continue', True, cfg.RED)
                if cfg.mouseClicked:
                    eventPos += 1
                    if eventPos > len(self.text) - 1: #advancing through the last page returns the function
                        if self.progression:
                            for i, v in self.progression.items():
                                cfg.PROGRESSIONDICT[i] = v
                        return
            cfg.DISPLAYSURF.blit(conSurf, conRect)

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ---------------------------- """

class ChoiceEvent(Event):
    """headache inducing event that has text like a text event, then variable options that lead to new events. """

    def __init__(self):
        super().__init__()

        self.type = 'Choice'
        self.text = [[]]
        self.choices = {} #keys are the choices that appear, vals are the tag for the event to be played directly after the choice
                        #note that 'Done' should be the val for a choice that ends the conversation and does nothing.

    def _playChoiceEvent(self, player, location):

        eventPos = 0
        while True:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayHud()

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

            #if there are pages of text remaining, the actions function like a simple text event
            #otherwise, the event choices are presented
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

    def _playInnEvent(self, player, location):

        #waits for you to choose yes or no
        action = None
        while not action:

            common_functions.standardEventHandling()

            location._locationBackground()
            player._displayHud()

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


""" ---------------------------- """
""" events """
#this is the current brute force way of creating events. hopefully i come up with ways to make it easier later, but this works for now

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
shannon.reqs = {'Shannon Concept': [0, 1]}

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
