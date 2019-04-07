
""" travel function for zth v1
      """

import pygame
import cfg, common_functions
import class_player
import class_game
import game_data

""" ------------------------------------------------------------------------ """

def main():

    player = class_player.Player('Phil')
    game = class_game.Game(player)
    destination = game_data.riverwood #uses astralis as a starting point and riverwood as a sample destination
    travelFunction(game, destination)


def travelFunction(game, destination):

    distance = common_functions.getDistance(game.coords, destination.coords)
    travelDaysNeeded = int(distance / 25) + 1
    daysTraveled = 0

    #in lieu of trig, this is the easier way to move the player day by day
    xDiff = destination.coords[0] - game.coords[0]
    yDiff = destination.coords[1] - game.coords[1]
    xChange = int(xDiff / travelDaysNeeded)
    yChange = int(yDiff / travelDaysNeeded)

    while daysTraveled < travelDaysNeeded:
        #can eventually make this more complicated so you arrive in town at a time related
        #to how many miles you had to travel on the last day
        travelEvent(game)
        daysTraveled += 1
        if daysTraveled < travelDaysNeeded:
            game.coords = (game.coords[0] + xChange, game.coords[1] + yChange)
            game.time = 20.5
            campScreen(game)

    game.coords = destination.coords
    game.time = 20
    return destination

""" ------------------------------------------------------------------------ """

def travelEvent(game):

    print('travel event happened')
    #travel events currently removed. need to add more and decide how they integrate into the game.

""" ------------------------------------------------------------------------ """

def campScreen(game):

    # nightCamp(game)
    game.day += 1
    game.time = 7
    # morningCamp(game)
    print('you slept a night at camp')

def nightCamp(game):

    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['Camp - Night'], (0,0))
        game._displayHud()

        optionBackSurf = pygame.Surface((200, 50))
        optionBackRect = optionBackSurf.get_rect()
        optionBackRect.topleft = (100, 100)
        sleepSurf = cfg.BASICFONT.render('Sleep', True, cfg.WHITE)
        sleepRect = sleepSurf.get_rect()
        sleepRect.midleft = (optionBackRect.left + 15, optionBackRect.centery)
        if optionBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            sleepSurf = cfg.BASICFONT.render('Sleep', True, cfg.RED)
            if cfg.mouseClicked:
                common_functions.fadeout(speed=15)
                return
        cfg.DISPLAYSURF.blit(optionBackSurf, optionBackRect)
        cfg.DISPLAYSURF.blit(sleepSurf, sleepRect)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def morningCamp(game):

    cfg.SOUNDDICT['Morning'].play()
    for i in range(255,0,-15):
        maskSurf = pygame.Surface((800, 600))
        maskSurf.fill(cfg.BLACK)
        maskSurf.set_alpha(i)
        cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['Camp - Day'], (0,0))
        cfg.DISPLAYSURF.blit(maskSurf, (0,0))

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)
    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['Camp - Day'], (0,0))
        game._displayHud()

        optionBackSurf = pygame.Surface((200, 50))
        optionBackRect = optionBackSurf.get_rect()
        optionBackRect.bottomright = (600, 400)
        resumeSurf = cfg.BASICFONT.render('Resume Trip', True, cfg.WHITE)
        resumeRect = resumeSurf.get_rect()
        resumeRect.midleft = (optionBackRect.left + 15, optionBackRect.centery)
        if optionBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            resumeSurf = cfg.BASICFONT.render('Resume Trip', True, cfg.RED)
            if cfg.mouseClicked:
                common_functions.fadeout(7)
                return
        cfg.DISPLAYSURF.blit(optionBackSurf, optionBackRect)
        cfg.DISPLAYSURF.blit(resumeSurf, resumeRect)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)




if __name__ == '__main__':
    main()
