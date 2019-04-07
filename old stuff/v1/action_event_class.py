
""" mission event class for zth """

import pygame, random
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class ActionEvent():
    def __init__(self):
        self.tag = ''
        self.type = ''
        self.text = []
        self.bg = pygame.image.load('images/bg/default.bmp')
        self.actions = {}

        self.eventBackRect = pygame.Rect(50, 75, 700, 400)

    def _displayActionEventBackground(self):

        cfg.DISPLAYSURF.blit(self.bg, (0,0))

        eventBackSurf = pygame.Surface((700, 400))
        eventBackSurf.fill(cfg.BLUE)
        eventBackSurf.set_alpha(220)
        eventBackRect = eventBackSurf.get_rect()
        eventBackRect.topleft = (50, 75)
        cfg.DISPLAYSURF.blit(eventBackSurf, eventBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, eventBackRect, 2)

    def _displayActionEventText(self, text):

        x = self.eventBackRect.left + 15
        y = self.eventBackRect.top + 15
        for i in text:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 28

    def _displayActionEventActions(self, last=True):

        x = self.eventBackRect.right - 25
        y = self.eventBackRect.bottom - 5
        if not last:
            actionSurf = cfg.BASICFONT.render('Next', True, cfg.WHITE)
            actionRect = actionSurf.get_rect()
            actionRect.bottomright = (x, y)
            if actionRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                actionSurf = cfg.BASICFONT.render('Next', True, cfg.RED)
                if cfg.mouseClicked:
                    return 'Next'
            cfg.DISPLAYSURF.blit(actionSurf, actionRect)
        elif not self.actions:
            doneSurf = cfg.BASICFONT.render('Done', True, cfg.WHITE)
            doneRect = doneSurf.get_rect()
            doneRect.bottomright = (x, y)
            if doneRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                doneSurf = cfg.BASICFONT.render('Done', True, cfg.RED)
                if cfg.mouseClicked:
                    return 'Done'
            cfg.DISPLAYSURF.blit(doneSurf, doneRect)
        else:
            for i in list(self.actions)[::-1]:
                actionSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
                actionRect = actionSurf.get_rect()
                actionRect.bottomright = (x, y)
                if actionRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    actionSurf = cfg.BASICFONT.render(i, True, cfg.RED)
                    if cfg.mouseClicked:
                        return self.actions[i]
                cfg.DISPLAYSURF.blit(actionSurf, actionRect)
                x -= 200

class StatEvent(ActionEvent):
    def __init__(self):
        super().__init__()

        self.type = 'Stat'
        self.affectedStats = []
        self.range = [0, 0]

    def _rollStatEvent(self, player):

        stat = random.choice(self.affectedStats)
        change = random.randint(self.range[0], self.range[1])

        player.stats[stat] += change

        if change > 0:
            buff = 'Increased'
        else:
            buff = 'Decreased'
        record = "Your %s was %s by %s!" % (stat, buff, abs(change))
        text = [
        " " ,
        record
        ]
        self.text[0] += text #this works as long as the conclusion event is one page, can look at a workaround if that comes up later


""" ------------------------------------------------------------------------ """
