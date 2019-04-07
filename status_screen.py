
""" game status screens for zth """

import pygame
import cfg, common_functions
import class_player
import class_game
import game_data

""" ------------------------------------------------------------------------ """

def main():

    player = class_player.Player('Phil')
    game = class_game.Game(player)
    game.bgImage = pygame.image.load('images/bg/default.bmp')
    game.activeJobs = [game_data.bear_hunt]
    game.activeJobs[0].startDay = 3
    game.player.classStats = {'Sword': 40 , 'Shield': 30, 'Heavy Armor': 35}
    game.player.stats = {'Health': 60 , 'Strength': 60, 'Endurance': 50, 'Intelligence': 30, 'Perception': 45, 'Focus': 40 ,
        'Charisma': 50, 'Stealth': 30, 'Speed': 40}
    game.player.weapon = 'Iron Sword'
    game.player.armor = 'Chain Mail'
    game.player.accessory = 'Bronze Ring'
    statusScreenMenu(game)


def statusScreenMenu(game):

    menu = ['Player', 'Time', 'Money', 'Inventory', 'Jobs', 'Return']

    while True:
        select = None

        common_functions.standardEventHandling()

        game._focusForeground()

        statusMenuBackSurf = pygame.Surface((250,325))
        statusMenuBackRect = statusMenuBackSurf.get_rect()
        statusMenuBackRect.midtop = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 8)
        cfg.DISPLAYSURF.blit(statusMenuBackSurf, statusMenuBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.BLUE, statusMenuBackRect, 2)

        x = statusMenuBackRect.centerx
        y = statusMenuBackRect.top + 20
        for i in menu:
            optionSurf = cfg.AR28.render(i, True, cfg.WHITE)
            optionRect = optionSurf.get_rect()
            optionRect.midtop = (x, y)
            if optionRect.collidepoint(cfg.mouseX, cfg.mouseY):
                optionSurf = cfg.AR28.render(i, True, cfg.RED)
                pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (optionRect.left + 5, optionRect.bottom + 1),
                    (optionRect.right - 5, optionRect.bottom + 1), 1)
                if cfg.mouseClicked:
                    select = i
            cfg.DISPLAYSURF.blit(optionSurf, optionRect)
            y += 50

        if select == 'Player':
            playerStatusScreen(game) #done

        elif select == 'Time':
            timeStatusScreen(game)

        elif select == 'Money':
            moneyStatusScreen(game)

        elif select == 'Inventory':
            invStatusScreen(game)

        elif select == 'Jobs':
            jobStatusScreen(game) #done

        elif select == 'Return' or cfg.rightClick:
            return

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def playerStatusScreen(game):

    while True:

        common_functions.standardEventHandling()

        game._focusForeground()

        backSurf = pygame.Surface((750, 560))
        backSurf.fill(cfg.BLACK)
        backSurf.set_alpha(220)
        backRect = backSurf.get_rect()
        backRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        mainCharInfoRect = pygame.Rect(backRect.left, backRect.top, backRect.width, 128)
        charStatusRect = pygame.Rect(backRect.left, mainCharInfoRect.bottom, 280, backRect.height - mainCharInfoRect.height)
        classStatusRect = pygame.Rect(charStatusRect.right, mainCharInfoRect.bottom, 250, backRect.height - mainCharInfoRect.height)
        statStatusRect = pygame.Rect(classStatusRect.right, mainCharInfoRect.bottom, 220, backRect.height - mainCharInfoRect.height)

        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, mainCharInfoRect, 1)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, charStatusRect, 1)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, classStatusRect, 1)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, statStatusRect, 1)

        #main character info
        charImageSurf = pygame.transform.scale(game.player.image, (120,120))
        charImageRect = charImageSurf.get_rect()
        charImageRect.topleft = (mainCharInfoRect.left + 4, mainCharInfoRect.top + 4)
        cfg.DISPLAYSURF.blit(charImageSurf, charImageRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, charImageRect, 1)

        charNameSurf = cfg.BASICFONT.render(game.player.name, True, cfg.WHITE)
        charNameRect = charNameSurf.get_rect()
        charNameRect.topleft = (charImageRect.right + 25, mainCharInfoRect.top + 10)
        charClassSurf = cfg.BASICFONT.render(game.player.playerClass, True, cfg.WHITE)
        charClassRect = charClassSurf.get_rect()
        charClassRect.topleft = (charImageRect.right + 25, charNameRect.bottom + 10)
        cfg.DISPLAYSURF.blit(charNameSurf, charNameRect)
        cfg.DISPLAYSURF.blit(charClassSurf, charClassRect)

        #char information stuff

        """this is a wip, this is stuff like affiliation info or even simple stats like gold/level, but i
            dont know what all goes here yet. im just gonna leave it blank for now i guess. """

        #class info stuff
        classStatsHeaderSurf = cfg.AR19.render('Class Stats: ', True, cfg.WHITE)
        classStatsHeaderRect = classStatsHeaderSurf.get_rect()
        classStatsHeaderRect.midtop = (classStatusRect.centerx, classStatusRect.top + 5)
        cfg.DISPLAYSURF.blit(classStatsHeaderSurf, classStatsHeaderRect)

        y = classStatsHeaderRect.bottom + 10
        for i, v in game.player.classStats.items():
            statNameSurf = cfg.AR17.render('%s: ' % i, True, cfg.WHITE)
            statNameRect = statNameSurf.get_rect()
            statNameRect.topleft = (classStatusRect.left + 10, y)
            statValSurf = cfg.AR17.render(str(v), True, cfg.WHITE)
            statValRect = statValSurf.get_rect()
            statValRect.topright = (classStatusRect.right - 30, y)
            cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
            cfg.DISPLAYSURF.blit(statValSurf, statValRect)
            y += 30

        equips = [game.player.weapon, game.player.armor, game.player.accessory]

        y += 10
        equipHeaderSurf = cfg.AR19.render('Equips:', True, cfg.WHITE)
        equipHeaderRect = equipHeaderSurf.get_rect()
        equipHeaderRect.midtop = (classStatusRect.centerx, y)
        cfg.DISPLAYSURF.blit(equipHeaderSurf, equipHeaderRect)
        y += 30
        for i in equips:
            itemNameSurf = cfg.AR17.render(i, True, cfg.WHITE)
            itemNameRect = itemNameSurf.get_rect()
            itemNameRect.topleft = (classStatusRect.left + 10, y)
            cfg.DISPLAYSURF.blit(itemNameSurf, itemNameRect)
            y += 30

        y += 10
        powerHeaderSurf = cfg.AR19.render('Power:', True, cfg.WHITE)
        powerHeaderRect = powerHeaderSurf.get_rect()
        powerHeaderRect.midtop = (classStatusRect.centerx, y)
        cfg.DISPLAYSURF.blit(powerHeaderSurf, powerHeaderRect)
        y += 30
        power = 0
        for i in game.player.classStats.values():
            power += v
        power = int(power / 3)
        powerSurf = cfg.AR25.render(str(power), True, cfg.WHITE)
        powerRect = powerSurf.get_rect()
        powerRect.midtop = (classStatusRect.centerx, y)
        cfg.DISPLAYSURF.blit(powerSurf, powerRect)

        #stat status
        otherStatsHeaderSurf = cfg.BASICFONT.render('Other Stats', True, cfg.WHITE)
        otherStatsHeaderRect = otherStatsHeaderSurf.get_rect()
        otherStatsHeaderRect.midtop = (statStatusRect.centerx, statStatusRect.top + 5)
        cfg.DISPLAYSURF.blit(otherStatsHeaderSurf, otherStatsHeaderRect)

        statTypeHeaders = ['Physical', 'Mental', 'Miscellaneous']
        otherStats5 = [
            [game.player.stats['Health'], game.player.stats['Strength'], game.player.stats['Endurance']] ,
            [game.player.stats['Intelligence'], game.player.stats['Perception'], game.player.stats['Focus']] ,
            [game.player.stats['Charisma'], game.player.stats['Stealth'], game.player.stats['Speed']]
        ]
        otherStats = [
            ['Health', 'Strength', 'Endurance'] , ['Intelligence', 'Perception', 'Focus'] , ['Charisma', 'Stealth', 'Speed']
        ]
        y = otherStatsHeaderRect.bottom + 5
        for i in range(0,3):
            statTypeHeaderSurf = cfg.BASICFONT.render('%s' % statTypeHeaders[i], True, cfg.WHITE)
            statTypeHeaderRect = statTypeHeaderSurf.get_rect()
            statTypeHeaderRect.topleft = (statStatusRect.left + 5, y)
            cfg.DISPLAYSURF.blit(statTypeHeaderSurf, statTypeHeaderRect)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (statStatusRect.left + 5, statTypeHeaderRect.top - 2),
                (statStatusRect.centerx + 25, statTypeHeaderRect.top - 2), 1)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (statStatusRect.left + 5, statTypeHeaderRect.bottom + 2),
                (statStatusRect.right - 5, statTypeHeaderRect.bottom + 2), 1)
            y += 40
            for j in otherStats[i]:
                statNameSurf = cfg.AR19.render('%s:' % j, True, cfg.WHITE)
                statNameRect = statNameSurf.get_rect()
                statNameRect.topleft = (statStatusRect.left + 10, y)
                statValSurf = cfg.AR19.render(str(game.player.stats[j]), True, cfg.WHITE)
                statValRect = statValSurf.get_rect()
                statValRect.topright = (statStatusRect.right - 25, y)
                cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
                cfg.DISPLAYSURF.blit(statValSurf, statValRect)
                y += 30

        if cfg.mouseClicked:
            return #will add a button later

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def jobStatusScreen(game):

    while True:

        common_functions.standardEventHandling()

        game._focusForeground()

        backSurf = pygame.Surface((700, 500))
        backSurf.fill(cfg.BLACK)
        backSurf.set_alpha(220)
        backRect = backSurf.get_rect()
        backRect.center = (cfg.WINWIDTH / 2, cfg.WINHEIGHT / 2)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        titleSurf = cfg.AR25.render('Job Status', True, cfg.WHITE)
        titleRect = titleSurf.get_rect()
        titleRect.midtop = (backRect.centerx, backRect.top + 10)
        cfg.DISPLAYSURF.blit(titleSurf, titleRect)

        headerBlockRect = pygame.Rect(backRect.left, titleRect.bottom, backRect.width, 32)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, headerBlockRect, 1)

        jobColumnRect = pygame.Rect(backRect.left, titleRect.bottom, 240, backRect.height - titleRect.height - 10)
        locationColumnRect = pygame.Rect(jobColumnRect.right, titleRect.bottom, 200, backRect.height - titleRect.height - 10)
        dayGivenColumnRect = pygame.Rect(locationColumnRect.right, titleRect.bottom, 130, backRect.height - titleRect.height - 10)
        dayDueColumnRect = pygame.Rect(dayGivenColumnRect.right, titleRect.bottom, 130, backRect.height - titleRect.height - 10)

        columnRects = [jobColumnRect, locationColumnRect, dayGivenColumnRect, dayDueColumnRect]
        headers = ['Job', 'Location', 'Start Day', 'Day Due']
        for i in range(0,4):
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, columnRects[i], 1)
            headerSurf = cfg.BASICFONT.render(headers[i], True, cfg.WHITE)
            headerRect = headerSurf.get_rect()
            headerRect.midtop = (columnRects[i].centerx, headerBlockRect.top + 5)
            cfg.DISPLAYSURF.blit(headerSurf, headerRect)

        y = headerBlockRect.bottom + 10
        for i in game.activeJobs:
            jobInfo = [i.jobName, i.hub, i.startDay, i.dueDay]
            for j in range(0, 4):
                infoSurf = cfg.BASICFONT.render(str(jobInfo[j]), True, cfg.WHITE)
                infoRect = infoSurf.get_rect()
                infoRect.midtop = (columnRects[j].centerx, y)
                cfg.DISPLAYSURF.blit(infoSurf, infoRect)
            y += 50

        if cfg.mouseClicked:
            return

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)


def timeStatusScreen(game):
    pass

def moneyStatusScreen(game):
    pass

def invStatusScreen(game):
    pass




""" ------------------------------------------------------------------------ """

if __name__ == '__main__':
    main()
