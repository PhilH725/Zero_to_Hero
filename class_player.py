
""" player class for zth """

import pygame
import cfg, common_functions

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
        self.weapon = ''
        self.armor = ''
        self.accessory = ''

""" ------------------------------------------------------------------------ """
