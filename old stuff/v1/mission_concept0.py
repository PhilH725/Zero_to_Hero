
""" mission concept for zth
      v0 """

import pygame, random
import cfg, common_functions, gameplay

""" ------------------------------------------------------------------------ """

class MissionEvent():
    def __init__(self):
        self.tag = ''
        self.type = ''
        self.text = []
        self.bg = pygame.image.load('images/bg/default.bmp')
        self.actions = {}

        self.eventBackRect = pygame.Rect(50, 75, 700, 400)

    def _displayMissionEventBackground(self):

        cfg.DISPLAYSURF.blit(self.bg, (0,0))

        eventBackSurf = pygame.Surface((700, 400))
        eventBackSurf.fill(cfg.BLUE)
        eventBackSurf.set_alpha(220)
        eventBackRect = eventBackSurf.get_rect()
        eventBackRect.topleft = (50, 75)
        cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 2)

    def _displayMissionEventText(self, text):

        x = self.eventBackRect.left + 15
        y = self.eventBackRect.top + 15
        for i in text:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 28

    def _displayMissionEventActions(self, last=True):

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

""" ------------------------ """

bear1 = MissionEvent()
bear1.tag = 'b01'
bear1.text = [
    ["You arrive in the forest ready to hunt the bear."]
]
bear1.actions = {'Go hunting': 'b02'}

bear2 = MissionEvent()
bear2.tag = 'b02'
bear2. text = [
    ["You find tracks and signs of a bear." ,
    "You follow them and eventually stumble upon a den."] ,
    ["Readying your weapon, you prepare to slay the beast that" ,
    "has been terrorizing the small town"]
]
bear2.actions = {'Fight the bear': 'b04'}

bear3 = MissionEvent()
bear3.tag = 'b03'
bear3. text = [
    ["You searched for hours and hours, but were" ,
    "unable to find anything, you return to Riverwood."]
]
bear3.actions = {'Return': 'End'}

MISSIONS = [bear1, bear2, bear3]

""" ------------------------------------------------------------------------ """

def main():

    player = gameplay.Player('Phil')
    mission = 'Bear Hunt'
    missionProcessing(player, mission)


def missionProcessing(player, mission):

    if mission == 'Bear Hunt':
        bearHunt(player)

def bearHunt(player):

    event = MISSIONS[0]
    while event:
        event = playMissionEvent(player, event)

        if event == 'b02':
            if player.stats['Perception'] >= 20:
                event = MISSIONS[1]
            else:
                event = MISSIONS[2]

def playMissionEvent(player, event):

    eventPos = 0
    while True:

        common_functions.standardEventHandling()

        event._displayMissionEventBackground()
        event._displayMissionEventText(event.text[eventPos])
        if eventPos > len(event.text) - 2:
            action = event._displayMissionEventActions()
        else:
            action = event._displayMissionEventActions(last=False)

        player._displayHud()

        if action:
            if action == 'Next':
                eventPos += 1
            elif action == 'End':
                return
            else:
                return action

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)



if __name__ == '__main__':
    main()
