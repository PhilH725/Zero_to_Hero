
""" travel event class
      these are separate from adventure events with their own display and handling, so better to keep there separate """

import pygame, random
import cfg, common_functions
import player_class
import travel_event_list

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil')
    travelEvent(player)


def travelEvent(player):

    eventGroup = random.choice(travel_event_list.TRAVELEVENTLIST)
    event = eventGroup[0]

    while True:

        result = playTravelEvent(player, event)
        if result == 'Done':
            return
        else:
            event = afterEvent(player, event, result, eventGroup)

def afterEvent(player, activeEvent, eventResult, eventGroup):

    eventResult = random.choice(eventResult)

    for i in eventGroup:
        if i.tag == eventResult:
            event = i

    if event.type == 'Stat':
        event._rollStatEvent(player)



    return event





def playTravelEvent(player, event):

    eventPos = 0
    while True:

        common_functions.standardEventHandling()

        event._displayActionEventBackground()
        event._displayActionEventText(event.text[eventPos])
        if eventPos == len(event.text) - 1:
            action = event._displayActionEventActions()
        else:
            action = event._displayActionEventActions(last=False)

        player._displayHud()

        if action:
            if action == 'Next':
                eventPos += 1
            else:
                return action

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

""" ------------------------------------------------------------------------ """

if __name__ == '__main__':
    main()
