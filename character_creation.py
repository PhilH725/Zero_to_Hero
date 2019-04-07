
""" character creation screen for zth v1 """

import pygame, os
import cfg, common_functions
import class_player

""" ------------------------------------------------------------------------ """

def main():

    player = characterCreationScreen()


def characterCreationScreen():

    player = class_player.Player('')

    basicInfoSlide(player)
    chooseClassSlide(player)

    return player

def basicInfoSlide(player):

    bgImage = pygame.image.load('images/bg/cc.bmp')

    aviList = []
    for i in os.listdir('./images/avi/cc'):
        avi = pygame.image.load('images/avi/cc/%s' % i)
        aviList.append(avi)

    index = 0
    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(bgImage, (0,0))

        backSurf = pygame.Surface((600,500))
        backSurf.set_alpha(220)
        backRect = backSurf.get_rect()
        backRect.topleft = (100, 50)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        instructSurf = cfg.BASICFONT.render('Enter your name: ', True, cfg.WHITE)
        instructRect = instructSurf.get_rect()
        instructRect.topleft = (backRect.left + 5, backRect.top + 5)
        cfg.DISPLAYSURF.blit(instructSurf, instructRect)

        nameEntrySurf = pygame.Surface((400, 40))
        nameEntrySurf.fill(cfg.BEIGE)
        nameEntrySurf.set_alpha(55)
        nameEntryRect = nameEntrySurf.get_rect()
        nameEntryRect.midtop = (cfg.WINWIDTH / 2, instructRect.bottom + 10)

        nameSurf = cfg.AR28.render(player.name, True, cfg.WHITE)
        nameRect = nameSurf.get_rect()
        nameRect.center = nameEntryRect.center

        cfg.DISPLAYSURF.blit(nameEntrySurf, nameEntryRect)
        cfg.DISPLAYSURF.blit(nameSurf, nameRect)

        x = backRect.left + 15
        y = nameEntryRect.bottom + 10
        for i in range(65,91):
            letterGridRect = pygame.Rect(x, y, 22, 30)
            letterSurf = cfg.BASICFONT.render('%s' % chr(i), True, cfg.WHITE)
            letterRect = letterSurf.get_rect()
            letterRect.center = letterGridRect.center
            cfg.DISPLAYSURF.blit(letterSurf, letterRect)
            if letterGridRect.collidepoint(cfg.mouseX, cfg.mouseY):
                pygame.draw.rect(cfg.DISPLAYSURF, cfg.RED, letterGridRect, 1)
                if cfg.mouseClicked:
                    player.name += chr(i)
            x += 30
            if x >= 580:
                x = backRect.left + 15
                y += 40

        x = backRect.left + 15
        y += 40
        for i in range(97, 123):
            letterGridRect = pygame.Rect(x, y, 22, 30)
            letterSurf = cfg.BASICFONT.render('%s' % chr(i), True, cfg.WHITE)
            letterRect = letterSurf.get_rect()
            letterRect.center = letterGridRect.center
            cfg.DISPLAYSURF.blit(letterSurf, letterRect)
            if letterGridRect.collidepoint(cfg.mouseX, cfg.mouseY):
                pygame.draw.rect(cfg.DISPLAYSURF, cfg.RED, letterGridRect, 1)
                if cfg.mouseClicked:
                    player.name += chr(i)
            x += 30
            if x >= 580:
                x = backRect.left + 15
                y += 40

        x += 10
        backspaceOutlineRect = pygame.Rect(x, y, 40, 30)
        backspaceSurf = cfg.AR15.render('DEL', True, cfg.WHITE)
        backspaceRect = backspaceSurf.get_rect()
        backspaceRect.center = (backspaceOutlineRect.centerx, backspaceOutlineRect.centery + 2)
        if backspaceOutlineRect.collidepoint(cfg.mouseX, cfg.mouseY):
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.RED, backspaceOutlineRect, 1)
            if cfg.mouseClicked:
                player.name = player.name[:-1]
        cfg.DISPLAYSURF.blit(backspaceSurf, backspaceRect)

        instructSurfTwo = cfg.BASICFONT.render('Choose your character image: ', True, cfg.WHITE)
        instructRectTwo = instructSurfTwo.get_rect()
        instructRectTwo.topleft = (backRect.left + 10, y + 40)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, y + 38), (backRect.right - 5, y + 38), 1)
        cfg.DISPLAYSURF.blit(instructSurfTwo, instructRectTwo)

        aviPreviewSurf = pygame.transform.scale(aviList[index], (144, 144))
        aviPreviewRect = aviPreviewSurf.get_rect()
        aviPreviewRect.midbottom = (backRect.left + (backRect.width / 4), backRect.bottom - 40)
        cfg.DISPLAYSURF.blit(aviPreviewSurf, aviPreviewRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, aviPreviewRect, 1)

        leftArrow = cfg.IMAGEDICT['Left One']
        leftArrowRect = leftArrow.get_rect()
        leftArrowRect.midright = (aviPreviewRect.left - 20, aviPreviewRect.centery)
        if leftArrowRect.collidepoint(cfg.mouseX, cfg.mouseY):
            leftArrow = cfg.IMAGEDICT['Left Two']
            if cfg.mouseClicked:
                index -= 1
                if index < 0:
                    index = len(aviList) - 1
        rightArrow = cfg.IMAGEDICT['Right One']
        rightArrowRect = rightArrow.get_rect()
        rightArrowRect.midleft = (aviPreviewRect.right + 20, aviPreviewRect.centery)
        if rightArrowRect.collidepoint(cfg.mouseX, cfg.mouseY):
            rightArrow = cfg.IMAGEDICT['Right Two']
            if cfg.mouseClicked:
                index += 1
                if index > len(aviList) - 1:
                    index = 0

        cfg.DISPLAYSURF.blit(leftArrow, leftArrowRect)
        cfg.DISPLAYSURF.blit(rightArrow, rightArrowRect)

        doneBackSurf = pygame.Surface((180, 75))
        doneBackSurf.fill(cfg.GREEN)
        doneBackSurf.set_alpha(45)
        doneBackRect = doneBackSurf.get_rect()
        doneBackRect.midright = (backRect.right - 50, aviPreviewRect.centery)
        doneSurf = cfg.AR25.render('Done', True, cfg.WHITE)
        doneRect = doneSurf.get_rect()
        doneRect.center = doneBackRect.center
        if doneBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and len(player.name) > 0:
            doneBackSurf.set_alpha(125)
            if cfg.mouseClicked:
                player.image = aviList[index]
                return
        cfg.DISPLAYSURF.blit(doneBackSurf, doneBackRect)
        cfg.DISPLAYSURF.blit(doneSurf, doneRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, doneBackRect, 1)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def chooseClassSlide(player):

    bgImage = pygame.image.load('images/bg/cc.bmp')

    jobClasses = ['Warrior', 'Mage', 'Rogue', 'Red Mage']
    index = 0

    classInfo = updateClassChoiceInfo(jobClasses[index])

    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(bgImage, (0,0))

        backSurf = pygame.Surface((700,500))
        backSurf.set_alpha(230)
        backRect = backSurf.get_rect()
        backRect.topleft = (50, 50)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        statBoxOutlineRect = pygame.Rect(backRect.centerx, backRect.top, backRect.width / 2, backRect.height)
        jobClassOutlineRect = pygame.Rect(backRect.left, backRect.top, backRect.width, backRect.height / 4)

        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, statBoxOutlineRect, 1)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, jobClassOutlineRect, 1)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left, backRect.bottom - 125), (backRect.centerx, backRect.bottom - 125), 1)

        instructSurf = cfg.BASICFONT.render('Choose your class: ', True, cfg.WHITE)
        instructRect = instructSurf.get_rect()
        instructRect.topleft = (backRect.left + 15, backRect.top + 5)
        cfg.DISPLAYSURF.blit(instructSurf, instructRect)

        jobClassSurf = cfg.AR28.render(jobClasses[index], True, cfg.WHITE)
        jobClassRect = jobClassSurf.get_rect()
        jobClassRect.center = (jobClassOutlineRect.left + jobClassOutlineRect.width / 4, jobClassOutlineRect.centery + 10)
        cfg.DISPLAYSURF.blit(jobClassSurf, jobClassRect)

        leftArrow = cfg.IMAGEDICT['Left One']
        leftArrowRect = leftArrow.get_rect()
        leftArrowRect.midleft = (jobClassOutlineRect.left + 20, jobClassRect.centery)
        if leftArrowRect.collidepoint(cfg.mouseX, cfg.mouseY):
            leftArrow = cfg.IMAGEDICT['Left Two']
            if cfg.mouseClicked:
                index -= 1
                if index < 0:
                    index = len(jobClasses) - 1
                classInfo = updateClassChoiceInfo(jobClasses[index])
        rightArrow = cfg.IMAGEDICT['Right One']
        rightArrowRect = rightArrow.get_rect()
        rightArrowRect.midright = ((jobClassOutlineRect.left + jobClassOutlineRect.width / 2) - 20, jobClassRect.centery)
        if rightArrowRect.collidepoint(cfg.mouseX, cfg.mouseY):
            rightArrow = cfg.IMAGEDICT['Right Two']
            if cfg.mouseClicked:
                index += 1
                if index > len(jobClasses) - 1:
                    index = 0
                classInfo = updateClassChoiceInfo(jobClasses[index])

        cfg.DISPLAYSURF.blit(leftArrow, leftArrowRect)
        cfg.DISPLAYSURF.blit(rightArrow, rightArrowRect)

        classStatsHeaderSurf = cfg.BASICFONT.render('Class Stats', True, cfg.WHITE)
        classStatsHeaderRect = classStatsHeaderSurf.get_rect()
        classStatsHeaderRect.midtop = (jobClassOutlineRect.centerx + jobClassOutlineRect.width / 4, jobClassOutlineRect.top + 10)
        cfg.DISPLAYSURF.blit(classStatsHeaderSurf, classStatsHeaderRect)

        y = classStatsHeaderRect.bottom + 5
        for i, v in classInfo[0].items():
            statNameSurf = cfg.AR19.render('%s:' % i, True, cfg.WHITE)
            statNameRect = statNameSurf.get_rect()
            statNameRect.topleft = (jobClassOutlineRect.centerx + 10, y)
            statValSurf = cfg.AR19.render(str(v), True, cfg.WHITE)
            statValRect = statValSurf.get_rect()
            statValRect.topright = (backRect.right - 25, y)
            cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
            cfg.DISPLAYSURF.blit(statValSurf, statValRect)
            y += 26

        otherStatsHeaderSurf = cfg.BASICFONT.render('Other Stats', True, cfg.WHITE)
        otherStatsHeaderRect = otherStatsHeaderSurf.get_rect()
        otherStatsHeaderRect.midtop = (statBoxOutlineRect.centerx, jobClassOutlineRect.bottom + 5)
        cfg.DISPLAYSURF.blit(otherStatsHeaderSurf, otherStatsHeaderRect)

        statTypeHeaders = ['Physical', 'Mental', 'Miscellaneous']
        y = otherStatsHeaderRect.bottom + 5
        for i in range(1,4):
            statTypeHeaderSurf = cfg.BASICFONT.render('%s' % statTypeHeaders[i - 1], True, cfg.WHITE)
            statTypeHeaderRect = statTypeHeaderSurf.get_rect()
            statTypeHeaderRect.topleft = (statBoxOutlineRect.left + 25, y)
            cfg.DISPLAYSURF.blit(statTypeHeaderSurf, statTypeHeaderRect)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (statBoxOutlineRect.left + 5, statTypeHeaderRect.top - 2),
                (statBoxOutlineRect.centerx + 25, statTypeHeaderRect.top - 2), 1)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (statBoxOutlineRect.left + 5, statTypeHeaderRect.bottom + 2),
                (statBoxOutlineRect.right - 5, statTypeHeaderRect.bottom + 2), 1)
            y += 30
            for j, v in classInfo[i].items():
                statNameSurf = cfg.AR19.render('%s:' % j, True, cfg.WHITE)
                statNameRect = statNameSurf.get_rect()
                statNameRect.topleft = (statBoxOutlineRect.left + 10, y)
                statValSurf = cfg.AR19.render(str(v), True, cfg.WHITE)
                statValRect = statValSurf.get_rect()
                statValRect.topright = (statBoxOutlineRect.right - 25, y)
                cfg.DISPLAYSURF.blit(statNameSurf, statNameRect)
                cfg.DISPLAYSURF.blit(statValSurf, statValRect)
                y += 26

        classDescriptionHeaderSurf = cfg.BASICFONT.render('Class Description: ', True, cfg.WHITE)
        classDescriptionHeaderRect = classDescriptionHeaderSurf.get_rect()
        classDescriptionHeaderRect.midtop = (backRect.left + backRect.width / 4, jobClassOutlineRect.bottom + 5)
        cfg.DISPLAYSURF.blit(classDescriptionHeaderSurf, classDescriptionHeaderRect)

        y = classDescriptionHeaderRect.bottom + 10
        for i in classInfo[4]:
            lineSurf = cfg.AR17.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (backRect.left + 10, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 24

        confirmMessageSurf = cfg.BASICFONT.render(classInfo[5], True, cfg.WHITE)
        confirmMessageRect = confirmMessageSurf.get_rect()
        confirmMessageRect.topleft = (backRect.left + 10, backRect.bottom - 120)
        cfg.DISPLAYSURF.blit(confirmMessageSurf, confirmMessageRect)

        confirmBackSurf = pygame.Surface((200, 60))
        confirmBackSurf.fill(cfg.GREEN)
        confirmBackSurf.set_alpha(45)
        confirmBackRect = confirmBackSurf.get_rect()
        confirmBackRect.midbottom = (backRect.left + backRect.width / 4, backRect.bottom - 20)
        confirmSurf = cfg.AR25.render('Confirm', True, cfg.WHITE)
        confirmRect = confirmSurf.get_rect()
        confirmRect.center = confirmBackRect.center
        if confirmBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            confirmBackSurf.set_alpha(125)
            if cfg.mouseClicked:
                player.playerClass = jobClasses[index]
                player.classStats = classInfo[0]
                for i in range(1,4):
                    for j, v in classInfo[i].items():
                        player.stats[j] = v
                return
        cfg.DISPLAYSURF.blit(confirmBackSurf, confirmBackRect)
        cfg.DISPLAYSURF.blit(confirmSurf, confirmRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, confirmBackRect, 1)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def updateClassChoiceInfo(className):
    """its this function or make a miniclass just for this. i think this is better. """

    if className == 'Warrior':
        combatStats = {'Sword': 40 , 'Shield': 30, 'Heavy Armor': 35}
        physStats = {'Health': 60 , 'Strength': 60, 'Endurance': 50}
        mentalStats = {'Intelligence': 30, 'Perception': 45, 'Focus': 40}
        miscStats = {'Charisma': 50, 'Stealth': 30, 'Speed': 40}
        classDescription = [
            "Warriors hit stuff with swords"
        ]
        confirmMessage = "You want to be a Warrior?"

    elif className == 'Mage':
        combatStats = {'Black Magic': 40 , 'Conjuration': 30, 'Alteration': 35}
        physStats = {'Health': 45 , 'Strength': 30, 'Endurance': 35}
        mentalStats = {'Intelligence': 60, 'Perception': 45, 'Focus': 60}
        miscStats = {'Charisma': 35, 'Stealth': 35, 'Speed': 40}
        classDescription = [
            "Mages make stuff go boom" ,
            "with magic."
        ]
        confirmMessage = "You want to be a Mage?"

    elif className == 'Rogue':
        combatStats = {'Archery': 40 , 'Knife': 30, 'Light Armor': 35}
        physStats = {'Health': 40 , 'Strength': 40, 'Endurance': 40}
        mentalStats = {'Intelligence': 30, 'Perception': 40, 'Focus': 50}
        miscStats = {'Charisma': 50, 'Stealth': 55, 'Speed': 55}
        classDescription = [
            "Rogues are agents of stealth and precision." ,
        ]
        confirmMessage = "You want to be a Rogue?"

    elif className == 'Red Mage':
        combatStats = {'Sword': 40 , 'Destruction': 30, 'Light Armor': 35}
        physStats = {'Health': 50 , 'Strength': 35, 'Endurance': 30}
        mentalStats = {'Intelligence': 60, 'Perception': 40, 'Focus': 50}
        miscStats = {'Charisma': 40, 'Stealth': 30, 'Speed': 40}
        classDescription = [
            "Masters of sword and magic, red mages" ,
            "have some of the highest potential for combat." ,
            "With that potential comes the cost of a much" ,
            "tougher to grasp art."
        ]
        confirmMessage = "You want to be a Red Mage?"

    classInfo = [combatStats, physStats, mentalStats, miscStats, classDescription, confirmMessage]
    return classInfo


""" ------------------------------------------------------------------------ """

if __name__ == '__main__':
    main()
