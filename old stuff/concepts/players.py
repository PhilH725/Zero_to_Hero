
""" player class for zth """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class Player():
    def __init__(self, name):
        self.name = name
        self.stats = {'Power': 50 , 'Strength': 25 , 'Perception': 40 , 'Endurance': 20 ,
                        'Charisma': 25 , 'Intelligence': 70}
        #ill make stats customizable later, theyre just on phil defaults for now

        self.gold = 1000
        self.day = 1 #this prob belongs in a game state object, but its the only thing for now so just putting it here.

        self.coords = (420, 315) #current location of the player. will match with a hub or be in the wilderness

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


#
