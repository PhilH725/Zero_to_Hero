
""" Zero to Hero v1 """

import pygame
import cfg
import common_functions
import title_screen
import main_menu
import adventure_mode
import hubs
import map
#import mission
import travel

""" ------------------------------------------------------------------------ """

def main():

    pygame.display.set_caption('Zero to Hero V1.0')

    title_screen.titleScreen()
    player = main_menu.mainMenuScreen()
    playGame(player)


def playGame(player):

    hub = hubs.HUBLIST[1]

    while True:
        newDest = None

        action = adventure_mode.adventureMode(player, hub)
        if action == 'World Map':
            newDest = map.worldMap(player)
            if newDest == 'Cancel':
                newDest = None
        elif action == 'Mission':
            mission.missionFunction()

        if newDest:
            hub = travel.travelFunction(player, newDest)


if __name__ == '__main__':
    main()
