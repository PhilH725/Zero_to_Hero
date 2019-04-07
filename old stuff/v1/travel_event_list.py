
""" contains the data for what makes up the travel events for zth. """

import pygame
import cfg, common_functions
import player_class
import action_event_class

""" ------------------------------------------------------------------------ """

water_nymph = action_event_class.ActionEvent()
water_nymph.tag = 'wn01'
water_nymph.type = 'Intro'
water_nymph.text = [
    ["While walking you hear a soft voice coming from a nearby pond. " ,
    "You investigate and find the source is a beautiful water nymph." ,
    " " ,
    "The creature playfully engages you and offers you a magical elixir." ,
    "She claims it will bring you great strength, but you're unsure whether" ,
    "you should trust the strange liquid or not."]
]
water_nymph.bg = pygame.image.load('images/bg/pond.bmp')
water_nymph.actions = {'Drink the elixir': ['wn03', 'wn04'], 'Refuse the drink': ['wn02']}

water_nymph_two = action_event_class.ActionEvent()
water_nymph_two.tag = 'wn02'
water_nymph_two.type = 'Text'
water_nymph_two.text = [
    ["Taking bizarre drinks from strangers seems like a bad idea. " ,
    "You refuse the elixir and continue on your way."]
]
water_nymph_two.bg = pygame.image.load('images/bg/pond.bmp')

water_nymph_three = action_event_class.StatEvent()
water_nymph_three.tag = 'wn03'
water_nymph_three.type = 'Stat'
water_nymph_three.text = [
    ["Trusting the water nymph, you drink the elixir..." ,
    " " ,
    "Power flows through your body as you suddenly feel invigorated!"]
]
water_nymph_three.bg = pygame.image.load('images/bg/pond.bmp')
water_nymph_three.affectedStats = ['Condition', 'Perception', 'Power']
water_nymph_three.range = [1, 7]

water_nymph_four = action_event_class.StatEvent()
water_nymph_four.tag = 'wn04'
water_nymph_four.type = 'Stat'
water_nymph_four.text = [
    ["Trusting the water nymph, you drink the elixir..." ,
    " " ,
    "You start to feel sick after drinking the strange liquid..." ,
    "A weakness envelopes your body. You are able to continue, but" ,
    "you feel worse."]
]
water_nymph_four.bg = pygame.image.load('images/bg/pond.bmp')
water_nymph_four.affectedStats = ['Condition', 'Perception', 'Power']
water_nymph_four.range = [-7, -1]

""" --- """




water_nymph_event = [water_nymph, water_nymph_two, water_nymph_three, water_nymph_four]
TRAVELEVENTLIST = [water_nymph_event]






#
