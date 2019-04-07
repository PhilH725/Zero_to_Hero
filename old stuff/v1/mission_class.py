
""" mission class for zth """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """

class Job():
    def __init__(self, jobName):
        self.jobName = jobName
        self.description = []
        self.reqs = {}
        self.distance = 0

    def _viewJobDetails(self):

        backSurf = pygame.Surface((600, 425))
        backSurf.fill(cfg.BLUE)
        backSurf.set_alpha(180)
        backRect = backSurf.get_rect()
        backRect.topleft = (100,50)

        titleSurf = cfg.AR25.render(self.missName, True, cfg.WHITE)
        titleRect = titleSurf.get_rect()
        titleRect.midtop = (backRect.centerx, backRect.top + 5)

        cfg.DISPLAYSURF.blit(backSurf, backRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, backRect, 2)

        cfg.DISPLAYSURF.blit(titleSurf, titleRect)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, titleRect.bottom + 5), (backRect.right - 5, titleRect.bottom + 5), 2)

        x = backRect.left + 10
        y = titleRect.bottom + 15
        for i in self.description:
            lineSurf = cfg.BASICFONT.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 35

        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, backRect.centery), (backRect.right - 5, backRect.centery), 2)

        skillReqSurf = cfg.AR19.render('Skill Recommendations: ', True, cfg.WHITE)
        skillReqRect = skillReqSurf.get_rect()
        skillReqRect.topleft = (backRect.left + 10, backRect.centery + 5)
        cfg.DISPLAYSURF.blit(skillReqSurf, skillReqRect)

        x = backRect.left + 5
        y = skillReqRect.bottom + 5
        for i, v in self.reqs.items():
            skillSurf = cfg.AR19.render('-%s: %s' % (i, v), True, cfg.WHITE)
            skillRect = skillSurf.get_rect()
            skillRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(skillSurf, skillRect)
            y += 28

        rewardHeaderSurf = cfg.AR19.render('Reward: ', True, cfg.WHITE)
        rewardHeaderRect = rewardHeaderSurf.get_rect()
        rewardHeaderRect.topright = (backRect.right - 50, backRect.centery + 5)
        cfg.DISPLAYSURF.blit(rewardHeaderSurf, rewardHeaderRect)

        x = backRect.right - 150
        y = rewardHeaderRect.bottom + 5
        for i, v in self.rewards.items():
            rewardSurf = cfg.AR19.render('-%s: %s' % (i, v), True, cfg.WHITE)
            rewardRect = rewardSurf.get_rect()
            rewardRect.topleft = (x, y)
            cfg.DISPLAYSURF.blit(rewardSurf, rewardRect)
            y += 28

        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (backRect.left + 5, backRect.bottom - 50), (backRect.right - 5, backRect.bottom - 50), 2)

        travelHeaderSurf = cfg.AR19.render('Travel Time (Days/One Way): ', True, cfg.WHITE)
        travelHeaderRect = travelHeaderSurf.get_rect()
        travelHeaderRect.bottomleft = (backRect.left + 25, backRect.bottom - 10)
        travelSurf = cfg.AR19.render('%s' % self.distance, True, cfg.WHITE)
        travelRect = travelSurf.get_rect()
        travelRect.bottomleft = (travelHeaderRect.right + 5, backRect.bottom - 10)
        cfg.DISPLAYSURF.blit(travelHeaderSurf, travelHeaderRect)
        cfg.DISPLAYSURF.blit(travelSurf, travelRect)

        acceptBackSurf = pygame.Surface((200, 65))
        acceptBackSurf.fill(cfg.GREEN)
        acceptBackSurf.set_alpha(80)
        acceptBackRect = acceptBackSurf.get_rect()
        acceptBackRect.topleft = (backRect.left + 50, backRect.bottom + 10)
        acceptSurf = cfg.AR25.render('Accept Mission', True, cfg.WHITE)
        acceptRect = acceptSurf.get_rect()
        acceptRect.center = acceptBackRect.center

        denyBackSurf = pygame.Surface((200, 65))
        denyBackSurf.fill(cfg.RED)
        denyBackSurf.set_alpha(80)
        denyBackRect = denyBackSurf.get_rect()
        denyBackRect.topright = (backRect.right - 50, backRect.bottom + 10)
        denySurf = cfg.AR25.render('Keep Looking', True, cfg.WHITE)
        denyRect = denySurf.get_rect()
        denyRect.center = denyBackRect.center

        if acceptBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            acceptBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Accept'

        if denyBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            denyBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Continue'

        cfg.DISPLAYSURF.blit(acceptBackSurf, acceptBackRect)
        cfg.DISPLAYSURF.blit(acceptSurf, acceptRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, acceptBackRect, 2)
        cfg.DISPLAYSURF.blit(denyBackSurf, denyBackRect)
        cfg.DISPLAYSURF.blit(denySurf, denyRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, denyBackRect, 2)
