
""" play event function for zth """

import pygame
import cfg, common_functions
import player_class
import event_list

""" ------------------------------------------------------------------------ """

def main():

    player = player_class.Player('Phil')
    player.bgImage = pygame.image.load('images/bg/default.bmp') #this is filled in through playing normally, so placeholder here
    event = event_list.innkeeper_generic
    playEvent(player, event)


def playEvent(player, event):
    """ takes an event and redirects to the proper handling based on the type of the event. """

    #plays text events with the class function
    if event.type == 'Text':
        event._playTextEvent(player)

    #plays choice events with the class function. note that choices lead to a recursion call
    elif event.type == 'Complex':
        cfg.activeComplexEvent = event
        choice = event._playComplexEvent(player)
        if choice == 'Done':
            return
        elif len(choice) == 2: #dont know the best way to call this out yet
            for i in event_list.EVENTLIST:
                if i.tag == choice[0]:
                    choiceResult = i
                    choiceResult._playContinuationEvent(player, choice[1])
            return
        else:
            #ill get to this later...
            playEvent(player, choiceResult)

    #plays inn events with class function
    elif event.type == 'Inn':
        event._playInnEvent(player)

    elif event.type == 'Shop':
        event._playShopEvent(player)

    elif event.type == 'Special':
        event._displayJobBoard(player)





#
