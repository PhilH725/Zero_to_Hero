
""" events for zth
      this does not include the class, is just the coding for filling out the events """

import pygame
import cfg, common_functions
import event_class
import job_class

""" ------------------------------------------------------------------------ """

""" --- """
#astralis

job_board = event_class.JobEvent()
job_board.displayName = 'Job Board'
job_board.image = pygame.image.load('images/job.png')
job_board.availableJobs = [job_class.bear_hunt, job_class.bandit_hunt]

amanda_main = event_class.TextEvent()
amanda_main.displayName = 'Guildmaster'
amanda_main.charName = 'Amanda'
amanda_main.image = pygame.image.load('images/avi/amanda.png')
amanda_main.text = [
    ["Hello, Phil. I trust you're keeping your skills sharp. I have a lot of" ,
    "new contracts coming in, there's room for advancement... if you" ,
    "can handle it."]
]

astralis_shopkeeper = event_class.ShopEvent()
astralis_shopkeeper.text = [
    "'Guild rate' doesn't mean free. What are you lookin to buy?"
]
astralis_shopkeeper.stock = {'Iron Sword': 100 , 'Iron Shield': 75}

zain_one = event_class.TextEvent()
zain_one.displayName = 'Zain'
zain_one.charName = 'Zain'
zain_one.image = pygame.image.load('images/avi/zain.png')
zain_one.text = [
    ["Hey Phil. Mel and I are flavor NPCs who will give you a little more" ,
    "information about the game and setting and stuff. But that will have",
    "to wait until more of the game is actually set."]
]

mel_one = event_class.TextEvent()
mel_one.displayName = 'Mel'
mel_one.charName = 'Mel'
mel_one.image = pygame.image.load('images/avi/mel.png')
mel_one.text = [
    ["Thinking of text for places like this is tough when so much is left",
    "undecided about the rest of the game..."]
]


dorm_bed = event_class.InnEvent()
dorm_bed.displayName = 'My bed'
dorm_bed.image = pygame.image.load('images/avi/zzz.png')
dorm_bed.price = 0
dorm_bed.text = ["Do you want to go to sleep?"]

""" --- """
#riverwood

innkeeper_generic = event_class.InnEvent()
innkeeper_generic.displayName = 'Innkeeper'
innkeeper_generic.charName = 'Innkeeper'
innkeeper_generic.image = pygame.image.load('images/avi/innkeeper.png')

riverwood_inn_guy = event_class.TextEvent()
riverwood_inn_guy.displayName = 'Guy'
riverwood_inn_guy.charName = 'Guy'
riverwood_inn_guy.image = pygame.image.load('images/avi/guy.png')
riverwood_inn_guy.text = [
    ["Riverwood's a nice, quiet place. Not too much" ,
    "goin on, but who wants everything to be all crazy?"] ,
    ["I don't have anything important to say, I'm just here" ,
    "to test text events."]
]

shannon_intro_one = event_class.TextEvent()
shannon_intro_one.displayName = 'Shannon'
shannon_intro_one.charName = 'Shannon'
shannon_intro_one.image = pygame.image.load('images/avi/shannon.png')
shannon_intro_one.text = [
    ["Hey Phil, where the fuck is Zach?" ,
    "He was supposed to be here twenty minutes ago. Go find him."]
]
shannon_intro_one.progression = {'Shannon Concept': 1}
shannon_intro_one.reqs = {'Shannon Concept': [0, 1]}

shannon_intro_two = event_class.TextEvent()
shannon_intro_one.displayName = 'Shannon'
shannon_intro_one.charName = 'Shannon'
shannon_intro_two.image = pygame.image.load('images/avi/shannon.png')
shannon_intro_two.text = [
    ["It's about time!" ,
    "I'm gonna kick your ass, Zach!"]
]
shannon_intro_two.reqs = {'Shannon Concept': [2]}

zach_intro_one = event_class.ComplexEvent()
zach_intro_one.displayName = 'Zach'
zach_intro_one.charName = 'Zach'
zach_intro_one.tag = 'z01'
zach_intro_one.image = pygame.image.load('images/avi/zach.png')
zach_intro_one.text = [
    ["Hey, how's it going? Shannon? Oh, I know she's waiting," ,
    "I was just hiding out here to piss her off."] ,
    ["You think we should go see her now?"]
]
zach_intro_one.choices = {'Yes': ['z02', '1'], 'No': ['z02', '2']}
zach_intro_one.reqs = {'Shannon Concept': [1]}

zach_con = event_class.ContinuationEvent()
zach_con.parent = 'z01'
zach_con.tag = 'z02'
zach_con.textOne = [
    ["Eh, I guess you're right, don't wanna piss her off 'too'",
    "much. Let's go."]
]
zach_con.textTwo = [
    ["Good call, it's so funny fucking with Shannon."] ,
    ["I am just gonna infinite loop until you say yes though," ,
    "so might wanna cut this off eventually."]
]
zach_con.progOne = {'Shannon Concept': 2}

zach_intro_three = event_class.MissionEvent()
zach_intro_one.displayName = 'Zach'
zach_intro_one.charName = 'Zach'
zach_intro_three.tag = 'z01'
zach_intro_three.image = pygame.image.load('images/avi/zach.png')
zach_intro_three.text = [
    ["Hey, how's it going? Shannon? Oh, I know she's waiting," ,
    "I was just hiding out here to piss her off."] ,
    ["You think we should go see her now?"]
]
zach_intro_three.choices = {'Yes': ['z02', '1'], 'No': ['z02', '2']}
zach_intro_three.reqs = {'Shannon Concept': [1]}

EVENTLIST = [innkeeper_generic, shannon_intro_one, shannon_intro_two, zach_intro_one, zach_con]
