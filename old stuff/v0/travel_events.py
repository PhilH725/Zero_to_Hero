
""" travel event class
      these are separate from adventure events with their own display and handling, so better to keep there separate """

import pygame, random
import cfg, common_functions, gameplay

""" ------------------------------------------------------------------------ """

class TravelEvent():
    def __init__(self):
        self.tag = ''
        self.type = ''
        self.text = []
        self.bg = pygame.image.load('images/bg/default.bmp')
        self.actions = {}

        self.eventBackRect = pygame.Rect(50, 75, 700, 400)

    def _displayTravelEventBackground(self):

        cfg.DISPLAYSURF.blit(self.bg, (0,0))

        eventBackSurf = pygame.Surface((700, 400))
        eventBackSurf.fill(cfg.BLUE)
        eventBackSurf.set_alpha(220)
        eventBackRect = eventBackSurf.get_rect()
        eventBackRect.topleft = (50, 75)
        cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 2)

    def _displayTravelEventText(self, text):

        x = self.eventBackRect.left + 15
        y = self.eventBackRect.top + 15
        for i in text:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 28

    def _displayTravelEventActions(self, last=True):

        x = self.eventBackRect.right - 25
        y = self.eventBackRect.bottom - 5
        if last:
            for i in list(self.actions)[::-1]:
                actionSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                actionRect = actionSurf.get_rect()
                actionRect.bottomright = (x, y)
                if actionRect.collidepoint(cfg.mouseX, cfg.mouseY):
                    actionSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                    if cfg.mouseClicked:
                        return self.actions[i]
                cfg.DISPLAYSURF.blit(actionSurf, actionRect)
                x -= 120
        else:
            actionSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
            actionRect = actionSurf.get_rect()
            actionRect.bottomright = (x, y)
            if actionRect.collidepoint(cfg.mouseX, cfg.mouseY):
                actionSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                if cfg.mouseClicked:
                    return 'Next'
            cfg.DISPLAYSURF.blit(actionSurf, actionRect)


""" ------------------------------- """

testEvent = TravelEvent()
testEvent.tag = 'te01'
testEvent.type = 'Intro'
testEvent.text = [
    ["This is a sample event." ,
    "There's nothing you can do besides advance to the next page."] ,
    ["I should be getting better at this stuff, so let's hope this works..."]
]
testEvent.actions = {'Okay': 'te02'}

te2 = TravelEvent()
te2.tag = 'te02'
te2.type = 'Text'
te2.text = [
    ["You have completed the event!"]
]
te2.actions = {'Continue': 'End'}

TRAVELEVENTLIST = [testEvent, te2]
TRAVELINTROEVENTLIST = []
for i in TRAVELEVENTLIST:
    if i.type == 'Intro':
        TRAVELINTROEVENTLIST.append(i)

""" ------------------------------------------------------------------------ """

def main():

    player = gameplay.Player('Phil')
    travelEvent(player)


def travelEvent(player):

    event = random.choice(TRAVELINTROEVENTLIST)

    while event:

        event = playTravelEvent(player, event)

def playTravelEvent(player, event):

    eventPos = 0
    while True:

        common_functions.standardEventHandling()

        event._displayTravelEventBackground()
        event._displayTravelEventText(event.text[eventPos])
        if eventPos > len(event.text) - 2:
            action = event._displayTravelEventActions()
        else:
            action = event._displayTravelEventActions(last=False)

        player._displayHud()

        if action:
            if action == 'Next':
                eventPos += 1
            elif action == 'End':
                return
            else:
                for i in TRAVELEVENTLIST:
                    if i.tag == action:
                        newEvent = i
                return newEvent

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

""" ------------------------------------------------------------------------ """

if __name__ == '__main__':
    main()
