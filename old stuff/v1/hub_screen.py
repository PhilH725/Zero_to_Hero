
""" hub screen for zth
      this isnt explicitly necessary, but helps keep things a little more in order. """

import pygame
import cfg, common_functions
import player_class
import hubs
import location_screen

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil')
    hub = hubs.HUBLIST[1] #uses Phil and Riverwood as default placeholders
    hubScreen(player, hub)


def hubScreen(player, hub):
    """ reads the given hub class object and displays available locations. also has options for returning options for world map or mission. """

    player.bgImage = hub.image

    while True:

        common_functions.standardEventHandling()

        action = hub._displayHubScreen() #main display for hub options
        player._displayHud() #always present main character hud

        if action:
            if action == 'World Map': #returned only if 'World Map' is selected
                return action
            else:
                location_screen.locationScreen(player, action) #location home screen

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)


if __name__ == '__main__':
    main()
