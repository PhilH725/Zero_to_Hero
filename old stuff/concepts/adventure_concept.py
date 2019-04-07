
""" main gameplay screen for zth v0
      this screen is where you control your character and can move around maps, talk to npcs and directly affect game state. """

import pygame
import cfg, common_functions, classes

def main():

    player = classes.Player('Phil')
    adventureScreen(player)


def adventureScreen(player):

    hub = classes.hubList[1]

    hubScreen(player, hub)

def hubScreen(player, hub):

    currentLocations = []
    for i in classes.locationList:
        if i.hub == hub.name:
            currentLocations.append(i)

    while True:

        common_functions.standardEventHandling()

        location = hub._displayHubScreen()
        player._displayPlayerStats()

        if location:
            if location == 'Leave':
                leaveScreen()
            else:
                for i in currentLocations:
                    if i.name == location:
                        location = i
                locationScreen(player, location)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def locationScreen(player, location):

    currentEvents = updateCurrentEvents(location)

    location.events = currentEvents #i can do this better later

    while True:

        common_functions.standardEventHandling()

        event = location._displayLocationScreen()
        player._displayPlayerStats()

        if event:
            if event == 'Leave':
                return
            else:
                playEvent(player, event, location)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def playEvent(player, event, location):
    """doesnt technically have to be its own function, but it keeps sorting events by type neater. """

    if event.type == 'Text':
        event._playTextEvent(player, location)

    elif event.type == 'Choice':
        choice = event._playChoiceEvent(player, location)
        if choice == 'Done':
            return
        for i in classes.EVENTLIST:
            if i.tag == choice:
                choiceResult = i
        playEvent(player, choiceResult, location)

    elif event.type == 'Inn':
        event._playInnEvent(player, location)

    return

def updateCurrentEvents(location):

    currentEvents = []
    for i in classes.EVENTLIST:
        if i.location == location.name:
            if i.reqs:
                reqsMet = True
                for j, v in i.reqs.items():
                    if cfg.PROGRESSIONDICT[j] not in v:
                        reqsMet = False
                if reqsMet:
                    currentEvents.append(i)
            else:
                currentEvents.append(i)

    return currentEvents





if __name__ == '__main__':
    main()
