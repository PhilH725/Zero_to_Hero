
""" travel function for zth v1
      """

import pygame
import cfg, common_functions
import player_class, hubs, travel_event

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil')
    destination = hubs.HUBLIST[2] #uses riverwood as a starting point and astralis hq as a sample destination
    travelFunction(player, destination)


def travelFunction(player, destination):

    distance = common_functions.getDistance(player.coords, destination.coords)
    travelDaysNeeded = int(distance / 25) + 1
    daysTraveled = 0

    #i dont have advanced trig knowledge, so this is the easier way to move the player day by day
    xDiff = destination.coords[0] - player.coords[0]
    yDiff = destination.coords[1] - player.coords[1]
    xChange = int(xDiff / travelDaysNeeded)
    yChange = int(yDiff / travelDaysNeeded)

    while daysTraveled < travelDaysNeeded:

        travel_event.travelEvent(player)
        daysTraveled += 1
        if daysTraveled < travelDaysNeeded:
            player.coords = (player.coords[0] + xChange, player.coords[1] + yChange)
            player.time = 20.5
            campScreen(player)

    player.coords = destination.coords
    player.time = 20
    return destination

def campScreen(player):

    nightCamp(player)
    morningCamp(player)

def nightCamp(player):

    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['Camp - Night'], (0,0))
        player._displayHud()

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

def morningCamp(player):

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
        player._displayHud()

        optionBackSurf = pygame.Surface((200, 50))
        optionBackRect = optionBackSurf.get_rect()
        optionBackRect.bottomright = (600, 400)
        resumeSurf = cfg.BASICFONT.render('Resume Trip', True, cfg.WHITE)
        resumeRect = resumeSurf.get_rect()
        resumeRect.midleft = (optionBackRect.left + 15, optionBackRect.centery)
        if optionBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            resumeSurf = cfg.BASICFONT.render('Resume Trip', True, cfg.RED)
            if cfg.mouseClicked:
                common_functions.fadeout()
                return
        cfg.DISPLAYSURF.blit(optionBackSurf, optionBackRect)
        cfg.DISPLAYSURF.blit(resumeSurf, resumeRect)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)




if __name__ == '__main__':
    main()
