
"""ZtH common functions."""

import pygame, sys, os, math
from pygame.locals import *
import cfg

"""--------------------------------------------------------------------------"""
#common functions

def getDistance(pointA, pointB):
    """ finds the pythagorean distance between two points """

    height = pointA[0] - pointB[0]
    length = pointA[1] - pointB[1]

    distance = int(math.sqrt( (height*height) + (length*length) ))
    return distance

def fadeout(speed=3):

    maskSurf = pygame.Surface((cfg.WINWIDTH , cfg.WINHEIGHT))
    maskSurf.fill(cfg.BLACK)
    for i in range(0, 255, speed):
        maskSurf.set_alpha(i)
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def fadein(speed = 3):

    maskSurf = pygame.Surface((cfg.WINWIDTH , cfg.WINHEIGHT))
    maskSurf.fill(cfg.BLACK)
    for i in range(0, 255, speed):
        maskSurf.set_alpha(i)
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)


def displayEventText(text, pos):
    """ displays the page of text at the given index. does not handle any of the other stuff like returning when done. """

    x = cfg.EVENTBOXRECT.left + 15
    y = cfg.EVENTAVIRECT.bottom + 15
    for i in text[pos]:
        lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
        lineRect = lineSurf.get_rect()
        lineRect.topleft = (x, y)
        cfg.DISPLAYSURF.blit(lineSurf, lineRect)
        y += 30

def drawTextBox():
    """draws the standard 750x125 textbox and places it at the standard position with 25 xpad and 10 ypad from bottom."""
    """for now im just making this function as is with no calibrations possible. can make it changeable later"""

    textbox = pygame.Surface((750, 125))
    textbox.set_alpha(180)
    textbox.fill(cfg.BLUE)
    textboxRect = textbox.get_rect()
    textboxRect.bottomleft = (25, cfg.WINHEIGHT - 10)

    cfg.DISPLAYSURF.blit(textbox, textboxRect)
    pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, textboxRect, 2)

def standardEventHandling():
    """saves space over constantly reusing the most common event handling menu"""

    cfg.mouseClicked = False
    cfg.rightClick = False

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == MOUSEMOTION:
            cfg.mouseX, cfg.mouseY = event.pos
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                cfg.mouseX, cfg.mouseY = event.pos
                cfg.mouseClicked = True
            elif event.button == 3:
                cfg.rightClick = True

def drawText(string, location, color, font):
    """takes a string and displays it at the given topleft location"""
    """this is just to display one string quickly, there are other functions to handle more in depth text blocks."""
    #note that this sample takes 4 args because im not importing config, usually color and font are default args.

    textSurface = font.render(string, True, color)
    textRect = textSurface.get_rect()
    textRect.topleft = location
    cfg.DISPLAYSURF.blit(textSurface, textRect)

def load_image(file_name, colorkey=False, image_directory='images'):
    'Loads an image, file_name, from image_directory, for use in pygame'
    file = os.path.join(image_directory, file_name)
    _image = pygame.image.load(file)
    if colorkey:
        if colorkey == -1:
        # If the color key is -1, set it to color of upper left corner
            colorkey = _image.get_at((0, 0))
        _image.set_colorkey(colorkey)
        _image = _image.convert()
    else: # If there is no colorkey, preserve the image's alpha per pixel.
        _image = _image.convert_alpha()
    return _image

def terminate():
    """properly exits pygame and the program."""
    pygame.quit()
    sys.exit()

"""--------------------------------------------------------------------------"""
