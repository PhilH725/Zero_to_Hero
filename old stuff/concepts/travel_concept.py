
""" travel function concept for zth v0
      """

import pygame
import cfg, common_functions, players, hubs

""" ------------------------------------------------------------------------ """

def main():

    player = players.Player('Phil')
    destination = hubs.HUBLIST[2]
    travelFunction(player, destination)


def travelFunction(player, destination):

    distanceRemaining = common_functions.getDistance(player.coords, destination.coords)
    daysTraveled = 0
    time = int(distanceRemaining / 25) + 1

    xDiff = destination.coords[0] - player.coords[0]
    yDiff = destination.coords[1] - player.coords[1]
    xChange = int(xDiff / time)
    yChange = int(yDiff / time)

    while distanceRemaining > 0:

        travelEvent()
        distanceRemaining -= 25
        if distanceRemaining > 0:
            player.coords = (player.coords[0] + xChange, player.coords[1] + yChange)
            campScreen(player)
    print('you have arrived')
    player.coords = destination.coords
    return destination

def travelEvent():

    print('a travel event happens')

def campScreen(player):

    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['Camp'], (0,0))
        player._displayPlayerStats()

        if cfg.mouseClicked:
            return


        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def movePlayer(player, destination):

    distance = common_functions.getDistance(player.coords, destination)
    time = int(distance / 25) + 1

    xDiff = destination.coords[0] - player.coords[0]
    yDiff = destination.coords[1] - player.coords[1]

    xChange = int(xDiff / time)
    yChange = int(yDiff / time)

    player.coords = (player.coords[0] + xChange, player.coords[1] + yChange)



if __name__ == '__main__':
    main()
