
""" location screen for zth
      again, just trying to keep things separated, offspring style. """

import pygame
import cfg, common_functions
import player_class
import locations
import play_event

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil') #default player
    location = locations.rwInn #test specific locations
    locationScreen(player, location)


def locationScreen(player, location):
    """ takes a location object, displays the main screen and handles options. """

    currentEvents = updateCurrentEvents(location) #reads progression/reqs and populates currently available events based on current location

    player.bgImage = location.image

    while True:

        common_functions.standardEventHandling()

        event = location._displayLocationScreen(currentEvents) #displays location background, events, options
        player._displayHud()

        if event:
            if event == 'Leave': #only returned if you choose to leave the location and return to the parent hub
                return
            else: #any other event goes to the function designed for handling events
                play_event.playEvent(player, event)
                currentEvents = updateCurrentEvents(location) #updates active events without having to reenter the location

        if cfg.rightClick and not cfg.hudMenu:
            return

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def updateCurrentEvents(location):
    """ receives the current location and determines which events are currently available. """

    currentEvents = []
    for i in location.events:
        if i.reqs: #additional handling required if an event has a reqs variable
            reqsMet = True
            for j, v in i.reqs.items():
                if cfg.PROGRESSIONDICT[j] not in v: #checks every req against its progression value
                    reqsMet = False #if any are met, the event is not added
            if reqsMet:
                currentEvents.append(i)
        else: #events with no reqs are always added
            currentEvents.append(i)

    return currentEvents









if __name__ == '__main__':
    main()
