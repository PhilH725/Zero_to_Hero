
""" game data for zth
      this is replacing what would normally be my game data folder, but these events are too complex to store that way. """

import pygame
import cfg, common_functions
import class_event
import class_location
import class_hub
import class_job

""" ------------------------------------------------------------------------ """

""" ------------------------------------- """
#jobs

bear_hunt = class_job.Job('Bear Hunt')
bear_hunt.jobName = 'Bear Hunt'
bear_hunt.hub = 'Riverwood'
bear_hunt.allowedTime = 7
bear_hunt.reqs = {'Power': 35, 'Perception': 35}
bear_hunt.contact = 'Huntsman Quartermaster'
bear_hunt.description = [
    "A large bear has been wreaking havoc in the countryside near Riverwood." ,
    "It has killed a local hunter and ransacked a food storage. The residents" ,
    "want it taken care of within the week. Bring the bear's pelt to the" ,
    "huntsman quartermaster to prove your work. Leads on location will be" ,
    "available through the quartermaster after arriving in Riverwood." ,
    "Ability to kill a bear and basic tracking knowledge are required."
]
bear_hunt.rewards = {'Gold': 150}

mission_one = class_job.Job('Mission One')
mission_one.reqs = {'Intelligence': 55, 'Health': 50}
mission_one.hub = 'Riverwood'
mission_one.description = []
mission_one.rewards = {'Gold': 300}

mission_two = class_job.Job('Mission Two')
mission_two.reqs = {'Sword': 40}
mission_two.hub = 'Azalea Town'
mission_two.description = []
mission_two.rewards = {'Gold': 200}

mission_three = class_job.Job('Mission Three')
mission_three.reqs = {'Charisma': 45, 'Street Skill': 50}
mission_three.hub = 'Inalta Deep'
mission_three.description = []
mission_three.rewards = {'Gold': 400}

mission_four = class_job.Job('Mission Four')
mission_four.reqs = {'Sword': 30, 'Armor': 30}
mission_four.hub = "Ivarstead"
mission_four.description = []
mission_four.rewards = {'Gold': 200}

bandit_hunt = class_job.Job('Bandit Hunt')
bandit_hunt.reqs = {'Power': 60}
bandit_hunt.distance = 5
bandit_hunt.description = [
    "Hunt bandits."
]
bandit_hunt.rewards = {'Gold': 200, 'Copper Sword': ''}

JOBLIST = [bear_hunt, bandit_hunt, mission_one, mission_two, mission_three, mission_four]

""" ------------------------------------- """
#events

""" --- """
#astralis

job_board = class_event.JobEvent()
job_board.displayName = 'Job Board'
job_board.image = pygame.image.load('images/avi/job.png')
job_board.availableJobs = [bear_hunt, bandit_hunt, mission_one, mission_two, mission_three, mission_four]

amanda_main = class_event.TextEvent()
amanda_main.displayName = 'Guildmaster'
amanda_main.charName = 'Amanda'
amanda_main.image = pygame.image.load('images/avi/amanda.png')
amanda_main.text = [
    ["Hello, Phil. I trust you're keeping your skills sharp. I have a lot of" ,
    "new contracts coming in, there's room for advancement... if you" ,
    "can handle it."]
]

astralis_shopkeeper = class_event.ShopEvent()
astralis_shopkeeper.text = [
    "'Guild rate' doesn't mean free. What are you lookin to buy?"
]
astralis_shopkeeper.stock = {'Iron Sword': 100 , 'Iron Shield': 75}

zain_one = class_event.TextEvent()
zain_one.displayName = 'Zain'
zain_one.charName = 'Zain'
zain_one.image = pygame.image.load('images/avi/zain.png')
zain_one.text = [
    ["Hey Phil. Mel and I are flavor NPCs who will give you a little more" ,
    "information about the game and setting and stuff. But that will have",
    "to wait until more of the game is actually set."]
]

mel_one = class_event.TextEvent()
mel_one.displayName = 'Mel'
mel_one.charName = 'Mel'
mel_one.image = pygame.image.load('images/avi/mel.png')
mel_one.text = [
    ["Thinking of text for places like this is tough when so much is left",
    "undecided about the rest of the game..."]
]

dorm_bed = class_event.InnEvent()
dorm_bed.displayName = 'My bed'
dorm_bed.image = pygame.image.load('images/avi/zzz.png')
dorm_bed.price = 0
dorm_bed.text = ["Do you want to go to sleep?"]

""" --- """
#riverwood

innkeeper_generic = class_event.InnEvent()
innkeeper_generic.displayName = 'Innkeeper'
innkeeper_generic.charName = 'Innkeeper'
innkeeper_generic.image = pygame.image.load('images/avi/innkeeper.png')

riverwood_inn_guy = class_event.TextEvent()
riverwood_inn_guy.displayName = 'Guy'
riverwood_inn_guy.charName = 'Guy'
riverwood_inn_guy.image = pygame.image.load('images/avi/guy.png')
riverwood_inn_guy.text = [
    ["Riverwood's a nice, quiet place. Not too much" ,
    "goin on, but who wants everything to be all crazy?"] ,
    ["I don't have anything important to say, I'm just here" ,
    "to test text events."]
]

riverwood_huntsman_quartermaster = class_event.TextEvent()
riverwood_huntsman_quartermaster.displayName = 'Huntsman Quartermaster'
riverwood_huntsman_quartermaster.charName = 'Huntsman Quartermaster'
riverwood_huntsman_quartermaster.image = pygame.image.load('images/avi/huntsman.png')
riverwood_huntsman_quartermaster.reqs = {'Bear Hunt': [0]}
riverwood_huntsman_quartermaster.progression = {'Bear Hunt': 1}
riverwood_huntsman_quartermaster.text = [
    ["You here to take care of that bear?" ,
    "That thing is a menace, no idea where it came from, but" ,
    "it's a tough one. We've tracked it, but it seems like it's" ,
    "multiple places at once sometimes."] ,
    ["We've tracked it close to it's den. I'll give you the details." ,
    "Bring that beast's pelt back and I'll gladly pay up."]
]

riverwood_huntsman_quartermaster_two = class_event.TextEvent()
riverwood_huntsman_quartermaster_two.displayName = 'Huntsman Quartermaster'
riverwood_huntsman_quartermaster_two.charName = 'Huntsman Quartermaster'
riverwood_huntsman_quartermaster_two.image = pygame.image.load('images/avi/huntsman.png')
riverwood_huntsman_quartermaster_two.reqs = {'Bear Hunt': [1]}
riverwood_huntsman_quartermaster_two.text = [
    ["Good luck with that bear."]
]

riverwood_hunter = class_event.TextEvent()
riverwood_hunter.displayName = 'Hunter'
riverwood_hunter.charName = 'Hunter'
riverwood_hunter.image = pygame.image.load('images/avi/hunter.png')
riverwood_hunter.text = [
    ["Riverwood is a small town and hunting is a big part of our" ,
    "economy. We trade food to Whiterun in exchange for supplies" ,
    "we can't get or make out here."]
]

""" ------------------------------------- """
#locations

""" --- """
#astralis

astralis_main_hall = class_location.Location()
astralis_main_hall.name = 'Main Hall'
astralis_main_hall.image = pygame.image.load('images/bg/main hall.png')
astralis_main_hall.events = [job_board]

astralis_gm_office = class_location.Location()
astralis_gm_office.name = "Guildmaster's Office"
astralis_gm_office.image = pygame.image.load('images/bg/gm office.bmp')
astralis_gm_office.events = [amanda_main]

astralis_training_room = class_location.Location()
astralis_training_room.name = 'Training Room'
astralis_training_room.image = pygame.image.load('images/bg/training room.bmp')
astralis_training_room.events = []

astralis_weapon_shop = class_location.Location()
astralis_weapon_shop.name = 'Guild Weapon Shop'
astralis_weapon_shop.image = pygame.image.load('images/bg/weapon shop.bmp')
astralis_weapon_shop.events = [astralis_shopkeeper]

astralis_tavern = class_location.Location()
astralis_tavern.name = 'Tavern'
astralis_tavern.image = pygame.image.load('images/bg/tavern-big.bmp')
astralis_tavern.events = []

astralis_hospital = class_location.Location()
astralis_hospital.name = 'Hospital'
astralis_hospital.image = pygame.image.load('images/bg/hospital.png')
astralis_hospital.events = []

astralis_library = class_location.Location()
astralis_library.name = 'Library'
astralis_library.image = pygame.image.load('images/bg/library.png')
astralis_library.events = [zain_one, mel_one]

astralis_homeroom = class_location.Location()
astralis_homeroom.name = 'Barracks - My Room'
astralis_homeroom.image = pygame.image.load('images/bg/my room.png')
astralis_homeroom.events = [dorm_bed]

""" --- """
#riverwood

riverwood_inn = class_location.Location()
riverwood_inn.name = 'Riverwood Inn'
riverwood_inn.image = pygame.image.load('images/bg/inn-small.bmp')
riverwood_inn.events = [innkeeper_generic, riverwood_inn_guy]

riverwood_tavern = class_location.Location()
riverwood_tavern.name = 'Riverwood Tavern'
riverwood_tavern.image = pygame.image.load('images/bg/tavern-small.png')
riverwood_tavern.events = []

riverwood_farm = class_location.Location()
riverwood_farm.name = 'Riverwood Farmhouse'
riverwood_farm.image = pygame.image.load('images/bg/farmhouse.bmp')
riverwood_farm.events = []

riverwood_hunting_hq = class_location.Location()
riverwood_hunting_hq.name = 'Hunting Headquarters'
riverwood_hunting_hq.image = pygame.image.load('images/bg/light building.bmp')
riverwood_hunting_hq.events = [riverwood_hunter, riverwood_huntsman_quartermaster]

""" --- """

""" ------------------------------------- """
#hubs

astralis = class_hub.Hub()
astralis.name = 'Astralis HQ'
astralis.image = pygame.image.load('images/bg/astralis.bmp')
astralis.locations = [astralis_main_hall, astralis_gm_office, astralis_training_room,
    astralis_weapon_shop, astralis_hospital, astralis_tavern, astralis_library, astralis_homeroom]
astralis.coords = (380, 280)

riverwood = class_hub.Hub()
riverwood.name = 'Riverwood'
riverwood.image = pygame.image.load('images/bg/riverwood.bmp')
riverwood.locations = [riverwood_inn, riverwood_tavern, riverwood_farm, riverwood_hunting_hq]
riverwood.coords = (420, 315)

solitude = class_hub.Hub()
solitude.name = 'Solitude'
solitude.image = pygame.image.load('images/bg/solitude.bmp')
solitude.locations = []
solitude.coords = (75, 75)

daggerfall = class_hub.Hub()
daggerfall.name = 'Daggerfall'
daggerfall.image = pygame.image.load('images/bg/daggerfall.bmp')
daggerfall.locations = []
daggerfall.coords = (65, 520)

cheydinhall = class_hub.Hub()
cheydinhall.name = 'Cheydinhall'
cheydinhall.image = pygame.image.load('images/bg/cheydinhall.bmp')
cheydinhall.locations = []
cheydinhall.coords = (680, 220)

kvatch = class_hub.Hub()
kvatch.name = 'Kvatch'
kvatch.image = pygame.image.load('images/bg/cheydinhall.bmp')
kvatch.locations = []
kvatch.coords = (500, 320)

anvil = class_hub.Hub()
anvil.name = 'Anvil'
anvil.image = pygame.image.load('images/bg/cheydinhall.bmp')
anvil.locations = []
anvil.coords = (300, 550)

HUBLIST = [astralis, riverwood, solitude, daggerfall, cheydinhall, kvatch, anvil]

""" ------------------------------------------------------------------------ """


#
