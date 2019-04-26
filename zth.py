
""" zth v2 """

import pygame
import cfg
import common_functions
import title_screen
import main_menu
import class_player
import class_game
import game_data
import adventure_mode
import job_mode
import map_mode
import travel_mode

""" ------------------------------------------------------------------------ """

def main():

    pygame.display.set_caption('Zero to Hero V2')

    title_screen.titleScreen()
    game = main_menu.mainMenuScreen()
    playGame(game)


def playGame(game):

    hub = game_data.astralis

    while True:
        newDest = None

        action = adventure_mode.adventureMode(game, hub)
        if action == 'World Map':
            newDest = map_mode.worldMap(game)
            if newDest == 'Cancel':
                newDest = None
        elif action[0] == 'Job':
            job_mode.jobFunction(game, action[1])

        if newDest:
            hub = travel_mode.travelFunction(game, newDest)


if __name__ == '__main__':
    main()
