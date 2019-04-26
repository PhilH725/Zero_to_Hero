
""" handles processing for jobs in zth """

import pygame
import cfg, common_functions
import class_player, class_game, game_data #this is just to make the main function work

""" ------------------------------------------------------------------------ """

def main():

    player = class_player.Player('Phil')
    game = class_game.Game(player)
    game.bgImage = pygame.image.load('images/bg/default.bmp')
    job = game_data.bear_hunt
    jobFunction(game, job)


def jobFunction(game, job):

    beforeJob(game)
    resultMessage = checkJobSuccess(game, job)
    afterJob(game, resultMessage)

def beforeJob(game):

    message = [
    "You arrive ready to work on this contract..."
    ]
    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(game.bgImage, (0,0))

        backSurf = pygame.Surface((600, 450))
        backSurf.fill(cfg.BLUE)
        backSurf.set_alpha(200)
        backRect = backSurf.get_rect()
        backRect.midtop = (cfg.WINWIDTH / 2, 25)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        y = backRect.top + 15
        for i in message:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (backRect.left + 10, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 30

        conBackSurf = pygame.Surface((150, 75))
        conBackRect = conBackSurf.get_rect()
        conBackRect.topright = (backRect.right - 15, backRect.bottom + 5)
        conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
        conRect = conSurf.get_rect()
        conRect.center = conBackRect.center
        if conBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            conBackSurf.fill(cfg.GREEN)
            conBackSurf.set_alpha(55)
            if cfg.mouseClicked:
                return
        cfg.DISPLAYSURF.blit(conBackSurf, conBackRect)
        cfg.DISPLAYSURF.blit(conSurf, conRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, conBackRect, 2)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)

def checkJobSuccess(game, job):

    success = True
    for i, v in job.reqs.items():
        if i in game.player.classStats:
            if game.player.classStats[i] < v:
                success = False
        elif i in game.player.stats:
            if game.player.stats[i] < v:
                success = False

    if success:
        job.workDays -= 1
        if job.workDays == 0:
            message = ['You completed the job!' , "Return to Astralis HQ for your payment."]
        else:
            message = ['You successfully work towards finishing the job.']
        cfg.PROGRESSIONDICT[job.jobName] = 3
    else:
        message = ['You failed to make progress on the job.']

    return message

def afterJob(game, message):

    while True:

        common_functions.standardEventHandling()

        cfg.DISPLAYSURF.blit(game.bgImage, (0,0))

        backSurf = pygame.Surface((600, 450))
        backSurf.fill(cfg.BLUE)
        backSurf.set_alpha(200)
        backRect = backSurf.get_rect()
        backRect.midtop = (cfg.WINWIDTH / 2, 25)
        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        y = backRect.top + 15
        for i in message:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (backRect.left + 10, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 30

        conBackSurf = pygame.Surface((150, 75))
        conBackRect = conBackSurf.get_rect()
        conBackRect.topright = (backRect.right - 15, backRect.bottom + 5)
        conSurf = cfg.BASICFONT.render('Continue', True, cfg.WHITE)
        conRect = conSurf.get_rect()
        conRect.center = conBackRect.center
        if conBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            conBackSurf.fill(cfg.GREEN)
            conBackSurf.set_alpha(55)
            if cfg.mouseClicked:
                return
        cfg.DISPLAYSURF.blit(conBackSurf, conBackRect)
        cfg.DISPLAYSURF.blit(conSurf, conRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, conBackRect, 2)

        pygame.display.update()
        cfg.FPSCLOCK.tick(cfg.FPS)


if __name__ == '__main__':
    main()
