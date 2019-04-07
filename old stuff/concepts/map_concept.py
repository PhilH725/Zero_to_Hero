
""" world map/travel start concept for zth v0
    """

import pygame, math
import cfg, common_functions, players, hubs

""" ------------------------------------------------------------------------ """

def main():

    player = players.Player('Phil')
    hub = hubs.HUBLIST[1]
    worldMap(player, hub)


def worldMap(player, hub):

    while True:

        common_functions.standardEventHandling()

        destination = displayMap(hub)

        if destination:
            action = mapMenu(player, hub, destination)
            if action == 'Start Trip':
                return destination

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def mapMenu(player, currentHub, destination):

    while True:

        common_functions.standardEventHandling()

        displayMapBackground(currentHub, destination)
        action = displayTravelMenu(player, currentHub, destination)

        if action:
            return action


        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def displayTravelMenu(player, currentHub, destination):

    distance = getDistance(currentHub.coords, destination.coords)
    time = int(distance / 25) + 1

    actions = ['Start Trip', 'Cancel']

    menuBackSurf = pygame.Surface((600, 350))
    menuBackSurf.fill(cfg.BLUE)
    menuBackSurf.set_alpha(220)
    menuBackRect = menuBackSurf.get_rect()
    menuBackRect.topleft = (100, 125)

    cfg.DISPLAYSURF.blit(menuBackSurf, menuBackRect)
    pygame.draw.rect(cfg.DISPLAYSURF, cfg.BLACK, menuBackRect, 2)

    headerSurf = cfg.AR25.render('Confirm Trip', True, cfg.WHITE)
    headerRect = headerSurf.get_rect()
    headerRect.midtop = (menuBackRect.centerx, menuBackRect.top + 5)
    cfg.DISPLAYSURF.blit(headerSurf, headerRect)
    pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (menuBackRect.left + 25, headerRect.bottom + 4),
        (menuBackRect.right - 25, headerRect.bottom + 4), 1)

    fromSurf = cfg.BASICFONT.render('Traveling from: %s' % currentHub.name, True, cfg.WHITE)
    fromRect = fromSurf.get_rect()
    fromRect.topleft = (menuBackRect.left + 10, headerRect.bottom + 10)
    toSurf = cfg.BASICFONT.render('Traveling to:     %s' % destination.name, True, cfg.WHITE)
    toRect = toSurf.get_rect()
    toRect.topleft = (menuBackRect.left + 10, fromRect.bottom + 10)
    cfg.DISPLAYSURF.blit(fromSurf, fromRect)
    pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (menuBackRect.left + 5, fromRect.bottom + 5),
        (headerRect.centerx + 25, fromRect.bottom + 5), 1)
    cfg.DISPLAYSURF.blit(toSurf, toRect)
    pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (menuBackRect.left + 5, toRect.bottom + 5),
        (headerRect.centerx + 25, toRect.bottom + 5), 1)

    distanceSurf = cfg.BASICFONT.render('Total Distance: %s miles' % distance, True, cfg.WHITE)
    distanceRect = distanceSurf.get_rect()
    distanceRect.topleft = (menuBackRect.left + 10, toRect.bottom + 12)
    cfg.DISPLAYSURF.blit(distanceSurf, distanceRect)
    pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (menuBackRect.left + 5, distanceRect.bottom + 5),
        (headerRect.centerx + 25, distanceRect.bottom + 5), 1)

    timeSurf = cfg.BASICFONT.render('Estimated Travel Time: %s days' % time, True, cfg.WHITE)
    timeRect = timeSurf.get_rect()
    timeRect.topleft = (menuBackRect.left + 10, distanceRect.bottom + 12)
    cfg.DISPLAYSURF.blit(timeSurf, timeRect)
    pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (menuBackRect.left + 5, timeRect.bottom + 5),
        (headerRect.centerx + 25, timeRect.bottom + 5), 1)

    x = menuBackRect.right - 15
    y = menuBackRect.bottom - 5
    for i in actions[::-1]:
        actionSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
        actionRect = actionSurf.get_rect()
        actionRect.bottomright = (x, y)
        if actionRect.collidepoint(cfg.mouseX, cfg.mouseY):
            actionSurf = cfg.BASICFONT.render(i, True, cfg.RED)
            if cfg.mouseClicked:
                return i
        cfg.DISPLAYSURF.blit(actionSurf, actionRect)
        x -= 100


def displayMapBackground(currentHub, destination):

    cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['World Map'], (0,0))

    for i in hubs.HUBLIST:
        if i == currentHub:
            hubRect = pygame.Rect(i.coords[0] - 15, i.coords[1] - 15, 30, 30)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLACK, i.coords, 15, 2)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.GREEN, i.coords, 8)
            nameSurf = cfg.AR15.render(i.name, True, cfg.BLACK)
            nameRect = nameSurf.get_rect()
            nameRect.midbottom = (i.coords[0], i.coords[1] - 5)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)
        elif i == destination:
            hubRect = pygame.Rect(i.coords[0] - 15, i.coords[1] - 15, 30, 30)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLACK, i.coords, 15, 2)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.RED, i.coords, 8)
            nameSurf = cfg.AR15.render(i.name, True, cfg.BLACK)
            nameRect = nameSurf.get_rect()
            nameRect.midbottom = (i.coords[0], i.coords[1] - 15)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)
        else:
            hubRect = pygame.Rect(i.coords[0] - 15, i.coords[1] - 15, 30, 30)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLACK, i.coords, 15, 2)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLUE, i.coords, 8)

    maskSurf = pygame.Surface((cfg.WINWIDTH, cfg.WINHEIGHT))
    maskSurf.fill(cfg.BLACK)
    maskSurf.set_alpha(40)
    cfg.DISPLAYSURF.blit(maskSurf, (0,0))

def displayMap(currentHub):

    cfg.DISPLAYSURF.blit(cfg.IMAGEDICT['World Map'], (0,0))

    for i in hubs.HUBLIST:
        if i == currentHub:
            hubRect = pygame.Rect(i.coords[0] - 15, i.coords[1] - 15, 30, 30)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLACK, i.coords, 15, 2)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.GREEN, i.coords, 8)
            nameSurf = cfg.AR15.render(i.name, True, cfg.BLACK)
            nameRect = nameSurf.get_rect()
            nameRect.midbottom = (i.coords[0], i.coords[1] - 5)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)
        else:
            hubRect = pygame.Rect(i.coords[0] - 15, i.coords[1] - 15, 30, 30)
            pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLACK, i.coords, 15, 2)
            if hubRect.collidepoint(cfg.mouseX, cfg.mouseY):
                pygame.draw.circle(cfg.DISPLAYSURF, cfg.RED, i.coords, 8)
                nameSurf = cfg.AR15.render(i.name, True, cfg.BLACK)
                nameRect = nameSurf.get_rect()
                nameRect.midbottom = (i.coords[0], i.coords[1] - 15)
                cfg.DISPLAYSURF.blit(nameSurf, nameRect)
                if cfg.mouseClicked:
                    return i
            else:
                pygame.draw.circle(cfg.DISPLAYSURF, cfg.BLUE, i.coords, 8)


def getDistance(a, b):

    height = a[0] - b[0]
    length = a[1] - b[1]

    distance = int(math.sqrt( (height*height) + (length*length) ))
    return distance







if __name__ == '__main__':
    main()
