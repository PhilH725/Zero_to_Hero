
""" zero to hero, version 0
    not a concept, but whatever i do here is probably gonna be reworked into a version 1 """

import pygame
import cfg, common_functions
import gameplay, hubs, locations, events, adventure_mode, map, travel

""" ------------------------------------------------------------------------ """

def main():

    player = gameplay.Player('Phil')
    mainGameLoop(player)


def mainGameLoop(player):

    hub = hubs.HUBLIST[1]

    while True:
        newDest = None

        action = adventure_mode.adventureMode(player, hub)
        if action == 'World Map':
            newDest = map.worldMap(player)
        elif action == 'Mission':
            #not implemented yet
            missionFunction()

        if newDest:
            hub = travel.travelFunction(player, newDest)











if __name__ == '__main__':
    main()
