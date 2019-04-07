
""" adventure mode v2
      im splitting things up a little differently this time, trying to make everything make more sequential sense
      now that i understand things a little more. """

import pygame
import cfg, common_functions
import player_class
import hubs
import hub_screen

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil')
    hub = hubs.HUBLIST[2] #uses Phil and Riverwood as default placeholders
    adventureMode(player, hub)


def adventureMode(player, hub):
    """ starts at the top level of adventure by displaying the current hub screen.
        hubScreen can return an option to enter the world map or mission functions. """

    while True:
        action = hub_screen.hubScreen(player, hub) #main screen

        #could just return action, but this helps visualize a little better whats happening
        if action == 'World Map':
            return 'World Map'
        elif action == 'Mission':
            return 'Mission'








if __name__ == '__main__':
    main()
