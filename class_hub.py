
""" hub class for zth """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """
#hub class

class Hub():
    def __init__(self):
        self.name = ''
        self.image = None
        self.locations = []
        self.coords = (0, 0)

    def _displayHubScreen(self, game):

        selectJobMenu = False
        while True:

            common_functions.standardEventHandling()

            #displays the main background image
            cfg.DISPLAYSURF.blit(self.image, (0,0))

            #displays the title/hub name
            nameBackSurf = pygame.Surface((280, 60))
            nameBackSurf.set_alpha(140)
            nameBackSurf.fill(cfg.BLACK)
            nameBackRect = nameBackSurf.get_rect()
            nameBackRect.midtop = (cfg.WINWIDTH / 2, 10)
            nameSurf = cfg.AR25.render(self.name, True, cfg.WHITE)
            nameRect = nameSurf.get_rect()
            nameRect.center = nameBackRect.center
            cfg.DISPLAYSURF.blit(nameBackSurf, nameBackRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, nameBackRect, 2)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)

            #displays all of the hubs possible location destinations. clicking returns the name of the location
            #currently runs off the screen for more than 12, ill deal with that when/if it happens, a lot isnt final yet.
            x = 20
            y = nameBackRect.bottom + 20
            counter = 1
            for i in self.locations:
                locationBackSurf = pygame.Surface((350, 60))
                locationBackSurf.set_alpha(160)
                locationBackSurf.fill(cfg.BLACK)
                locationBackRect = locationBackSurf.get_rect()
                locationBackRect.topleft = (x, y)

                locSurf = cfg.BASICFONT.render(i.name, True, cfg.WHITE)
                locRect = locSurf.get_rect()
                locRect.midleft = (locationBackRect.left + 25, locationBackRect.centery)
                if locationBackRect.collidepoint(cfg.mouseX, cfg.mouseY) and not cfg.hudMenu:
                    locationBackSurf.fill(cfg.BLUE)
                    locationBackSurf.set_alpha(55)
                    locSurf = cfg.BASICFONT.render(i.name, True, cfg.RED)
                    if cfg.mouseClicked:
                        return ['Location', i]

                cfg.DISPLAYSURF.blit(locationBackSurf, locationBackRect)
                cfg.DISPLAYSURF.blit(locSurf, locRect)
                pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, locationBackRect, 2)
                y += 65
                counter += 1
                if counter == 6:
                    x = (cfg.WINWIDTH / 2) + 20
                    y = nameBackRect.bottom + 20

            #special hub options (access jobs available from that hub or the world map)
            pygame.draw.line(cfg.DISPLAYSURF, cfg.BLUE, (5, 480), (cfg.WINWIDTH - 5, 480), 2)

            hubJobs = []
            for i in game.activeJobs:
                if i.hub == self.name:
                    hubJobs.append(i)

            if hubJobs:
                doJobBackSurf = pygame.Surface((350, 60))
                doJobBackSurf.set_alpha(160)
                doJobBackSurf.fill(cfg.BLACK)
                doJobBackRect = doJobBackSurf.get_rect()
                doJobBackRect.bottomleft = (20, 480)
                doJobSurf = cfg.BASICFONT.render('Work on Job', True, cfg.WHITE)
                doJobRect = doJobSurf.get_rect()
                doJobRect.center = doJobBackRect.center
                if doJobBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
                    doJobBackSurf.fill(cfg.GREEN)
                    doJobBackSurf.set_alpha(55)
                    doJobSurf = cfg.BASICFONT.render('Work on Job', True, cfg.RED)
                    if cfg.mouseClicked:
                        if len(hubJobs) == 1:
                            return ['Job', hubJobs[0]]
                        else:
                            jobChoice = self._selectJobMenu(game, hubJobs)
                            return ['Job', jobChoice]
                cfg.DISPLAYSURF.blit(doJobBackSurf, doJobBackRect)
                cfg.DISPLAYSURF.blit(doJobSurf, doJobRect)
                pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, doJobBackRect, 2)

            leaveBackSurf = pygame.Surface((350, 60))
            leaveBackSurf.set_alpha(160)
            leaveBackSurf.fill(cfg.BLACK)
            leaveBackRect = leaveBackSurf.get_rect()
            leaveBackRect.bottomleft = ((cfg.WINWIDTH / 2) + 20, 480)
            leaveSurf = cfg.BASICFONT.render('World Map', True, cfg.WHITE)
            leaveRect = leaveSurf.get_rect()
            leaveRect.center = leaveBackRect.center
            if leaveBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
                leaveBackSurf.fill(cfg.GREEN)
                leaveBackSurf.set_alpha(55)
                leaveSurf = cfg.BASICFONT.render('World Map', True, cfg.RED)
                if cfg.mouseClicked:
                    return ['World Map']
            cfg.DISPLAYSURF.blit(leaveBackSurf, leaveBackRect)
            cfg.DISPLAYSURF.blit(leaveSurf, leaveRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, leaveBackRect, 2)

            game._displayHud()

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

    def _selectJobMenu(self, game, jobs):

        while True:

            common_functions.standardEventHandling()

            cfg.DISPLAYSURF.blit(self.image, (0,0))

            nameBackSurf = pygame.Surface((280, 60))
            nameBackSurf.set_alpha(140)
            nameBackSurf.fill(cfg.BLACK)
            nameBackRect = nameBackSurf.get_rect()
            nameBackRect.midtop = (cfg.WINWIDTH / 2, 10)
            nameSurf = cfg.AR25.render(self.name, True, cfg.WHITE)
            nameRect = nameSurf.get_rect()
            nameRect.center = nameBackRect.center
            cfg.DISPLAYSURF.blit(nameBackSurf, nameBackRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, nameBackRect, 2)
            cfg.DISPLAYSURF.blit(nameSurf, nameRect)

            backSurf = pygame.Surface((400, 475))
            backSurf.fill(cfg.BLACK)
            backSurf.set_alpha(120)
            backRect = backSurf.get_rect()
            backRect.midtop = (cfg.WINWIDTH / 2, 100)
            cfg.DISPLAYSURF.blit(backSurf, backRect)
            pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

            y = backRect.top + 15
            for i in jobs:
                jobBackSurf = pygame.Surface((380, 80))
                jobBackSurf.fill(cfg.BLUE)
                jobBackSurf.set_alpha(55)
                jobBackRect = jobBackSurf.get_rect()
                jobBackRect.midtop = (backRect.centerx, y)
                jobSurf = cfg.AR25.render(i.jobName, True, cfg.WHITE)
                jobRect = jobSurf.get_rect()
                jobRect.midleft = (jobBackRect.left + 15, jobBackRect.centery)
                if jobBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
                    jobBackSurf.set_alpha(205)
                    if cfg.mouseClicked:
                        return i
                cfg.DISPLAYSURF.blit(jobBackSurf, jobBackRect)
                pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, jobBackRect, 1)
                cfg.DISPLAYSURF.blit(jobSurf, jobRect)
                y += 100

            pygame.display.update()
            cfg.FPSCLOCK.tick(cfg.FPS)

""" ------------------------------------------------------------------------ """
