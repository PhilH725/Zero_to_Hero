
""" adventure mode v2
      im splitting things up a little differently this time, trying to make everything make more sequential sense
      now that i understand things a little more. """

import pygame
import cfg, common_functions
import class_player
import class_game
import game_data

""" ------------------------------------------------------------------------ """

def main():

    player = class_player.Player('Phil')
    game = class_game.Game(player)
    location = game_data.astralis_library #uses Phil and Riverwood as default placeholders
    locationScreen(game, location)


def locationScreen(game, location):
    """ takes a location object, displays the main screen and handles options. """

    currentEvents = updateCurrentEvents(location)

    game.bgImage = location.image

    while True:

        common_functions.standardEventHandling()

        event = location._displayLocationScreen(currentEvents) #displays location background, events, options

        if event:
            if event == 'Leave': #only returned if you choose to leave the location and return to the parent hub
                return
            else: #any other event goes to the function designed for handling events
                playEvent(game, event)
                currentEvents = updateCurrentEvents(location) #updates active events without having to reenter the location

        if cfg.rightClick and not cfg.hudMenu:
            return

        game._displayHud()

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def updateCurrentEvents(location):
    """ receives the current location and determines which events are currently available. """

    currentEvents = []
    for i in location.events:
        if i.reqs: #additional handling required if an event has a reqs variable
            reqsMet = True
            for j, v in i.reqs.items():
                if j in cfg.PROGRESSIONDICT:
                    if cfg.PROGRESSIONDICT[j] not in v: #checks every req against its progression value
                        reqsMet = False #if any are met, the event is not added
                else:
                    reqsMet = False
            if reqsMet:
                currentEvents.append(i)
        else: #events with no reqs are always added
            currentEvents.append(i)

    return currentEvents

def playEvent(game, event):
    """ takes an event and redirects to the proper handling based on the type of the event. """

    #plays text events with the class function
    if event.type == 'Text':
        event._playTextEvent(game)

    #plays choice events with the class function. note that choices lead to a recursion call
    elif event.type == 'Complex':
        cfg.activeComplexEvent = event
        choice = event._playComplexEvent(game)
        if choice == 'Done':
            return
        elif len(choice) == 2: #dont know the best way to call this out yet
            for i in event_list.EVENTLIST:
                if i.tag == choice[0]:
                    choiceResult = i
                    choiceResult._playContinuationEvent(game, choice[1])
            return
        else:
            #ill get to this later...
            playEvent(game, choiceResult)

    #plays inn events with class function
    elif event.type == 'Inn':
        event._playInnEvent(game)

    elif event.type == 'Shop':
        event._playShopEvent(game)

    elif event.type == 'Special':
        event._displayJobBoard(game)

""" ------------------------------------------------------------------------ """

if __name__ == '__main__':
    main()
