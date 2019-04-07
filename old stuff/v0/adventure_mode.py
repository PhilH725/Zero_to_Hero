
""" adventure mode screen/gameplay for zth v1
      """

import pygame
import cfg, common_functions
import gameplay, hubs, locations, events

""" ------------------------------------------------------------------------ """

def main():

    player = gameplay.Player('Phil')
    hub = hubs.HUBLIST[1] #use Phil and Riverwood as default placeholders
    adventureMode(player, hub)


def adventureMode(player, hub):
    """ topmost layer of adventure. """

    while True:
        action = hubScreen(player, hub) #main screen

        if action == 'Leave':
            return 'World Map'
        elif action == 'Mission':
            #not implemented yet
            return 'Mission'

def hubScreen(player, hub):
    """ reads the given hub class object and displays available locations. also has options for opening the world map or working on a mission. """

    while True:

        common_functions.standardEventHandling()

        location = hub._displayHubScreen() #main display for hub options
        player._displayHud() #always present main character hud

        if location:
            if location == 'Leave': #returned only if 'Leave Hub' is selected
                return 'Leave'
            else:
                for i in locations.LOCLIST: #probably a better way to do this, but connects dots to lead into the correct location
                    if i.name == location and i.hub == hub.name:
                        location = i
                locationScreen(player, location) #location home screen

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def locationScreen(player, location):
    """ takes a location object, displays the main screen and handles options. """

    currentEvents = updateCurrentEvents(location) #reads progression/reqs and populates currently available events based on current location

    while True:

        common_functions.standardEventHandling()

        event = location._displayLocationScreen() #displays location background, events, options
        player._displayHud()

        if event:
            if event == 'Leave': #only returned if you choose to leave the location and return to the parent hub
                return
            else: #any other event goes to the function designed for handling events
                playEvent(player, event, location)
                currentEvents = updateCurrentEvents(location) #updates active events without having to reenter the location

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def playEvent(player, event, location):
    """ takes an event and redirects to the proper handling based on the type of the event. """
    #location is kept as a parameter to display the proper background. that could be handled by looping through and checking
    #for matching location names through the events, but this is simpler.

    #plays text events with the class function
    if event.type == 'Text':
        event._playTextEvent(player, location)

    #plays choice events with the class function. note that choices lead to a recursion call
    elif event.type == 'Choice':
        choice = event._playChoiceEvent(player, location)
        if choice == 'Done':
            return
        for i in events.EVENTLIST:
            if i.tag == choice:
                choiceResult = i
        playEvent(player, choiceResult, location)

    #plays inn events with class function
    elif event.type == 'Inn':
        event._playInnEvent(player, location)

def updateCurrentEvents(location):
    """ receives the current location and reads the global EVENTLIST to determine which events are currently available. """

    currentEvents = []
    for i in events.EVENTLIST: #parses through every event. might be a way to reduce the size here later
        if i.location == location.name: #only looks at events in this location.
            if i.reqs: #additional handling required if an event has a reqs variable
                reqsMet = True
                for j, v in i.reqs.items():
                    if cfg.PROGRESSIONDICT[j] not in v: #checks every req against its progression value
                        reqsMet = False #if any are met, the event is not added
                if reqsMet:
                    currentEvents.append(i)
            else: #events with no reqs are added based only on location
                currentEvents.append(i)

    location.events = currentEvents #updates location class
    return currentEvents



if __name__ == '__main__':
    main()
