
"""ZtH config file"""

import pygame, sys, os

#simple constants
WINWIDTH = 800
WINHEIGHT = 600
FPS = 30
#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)
GRAY = (128, 128, 128)
BEIGE = (255, 255, 120)
PINK = (255, 0, 200)

#game options
MAINMENUOPTIONS = ['Quick Play', 'Create Character', 'Load Game', 'Options', 'Exit Game']

#system
mouseX = 0
mouseY = 0
mouseClicked = False
rightClick = False

#game flow
hudMenu = False

activeComplexEvent = None

#game progression
PROGRESSIONDICT = {'NaN': 0, 'Shannon Concept': 0}

MISSIONDICT = {'Bear Hunt': 0}

#main pygame constants. note that pygame still needs initialized within any program using it
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))

#fonts
BASICFONT = pygame.font.SysFont('Arial', 21)
AR15 = pygame.font.SysFont('Arial', 15)
AR17 = pygame.font.SysFont('Arial', 17)
AR19 = pygame.font.SysFont('Arial', 19)
AR21 = pygame.font.SysFont('Arial', 21)
AR25 = pygame.font.SysFont('Arial', 25)
AR28 = pygame.font.SysFont('Arial', 28)
AR32 = pygame.font.SysFont('Arial', 32)
AR40 = pygame.font.SysFont('Arial', 40)
AR52 = pygame.font.SysFont('Arial', 52)
AR74 = pygame.font.SysFont('Arial', 74)
CA21 = pygame.font.SysFont('Calibri', 21)
CA30 = pygame.font.SysFont('Calibri', 30)
CA36 = pygame.font.SysFont('Calibri', 36)
CA42 = pygame.font.SysFont('Calibri', 21)


IMAGEDICT = {
    'World Map': pygame.image.load('images/misc/map.jpg') ,
    'Camp - Night': pygame.image.load('images/bg/camp-night.bmp') ,
    'Camp - Day': pygame.image.load('images/bg/camp-day.bmp') ,
    'Right One': pygame.image.load('images/misc/right1.jpg') ,
    'Right Two': pygame.image.load('images/misc/right2.jpg') ,
    'Left One': pygame.image.load('images/misc/left1.jpg') ,
    'Left Two': pygame.image.load('images/misc/left2.jpg') ,
}

#sounds
SOUNDDICT = {
    'Inn': pygame.mixer.Sound('se/inn.ogg') ,
    'Morning': pygame.mixer.Sound('se/morning.ogg')
}

#
