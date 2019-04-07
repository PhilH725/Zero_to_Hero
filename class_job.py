
""" job class for zth """

import pygame
import cfg, common_functions

""" ------------------------------------------------------------------------ """
# job class

class Job():
    def __init__(self, jobName):
        self.jobName = jobName
        self.description = []
        self.hub = ''
        self.allowedTime = 0
        self.startDay = 0
        self.dueDay = 0
        self.workDays = 1
        self.reqs = {}
        self.contact = ''
        self.distance = 0
        self.rewards = {}

    def _jobPosting(self):

        #job title
        jobBackSurf = pygame.Surface((650, 480))
        jobBackSurf.fill(cfg.BLUE)
        jobBackSurf.set_alpha(180)
        jobBackRect = jobBackSurf.get_rect()
        jobBackRect.topleft = (75,10)
        cfg.DISPLAYSURF.blit(jobBackSurf, jobBackRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, jobBackRect, 2)

        jobTitleSurf = cfg.AR21.render(self.jobName, True, cfg.WHITE)
        jobTitleRect = jobTitleSurf.get_rect()
        jobTitleRect.midtop = (jobBackRect.centerx, jobBackRect.top + 5)
        cfg.DISPLAYSURF.blit(jobTitleSurf, jobTitleRect)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobBackRect.left + 5, jobTitleRect.bottom + 5),
            (jobBackRect.right - 5, jobTitleRect.bottom + 5), 2)

        y = jobTitleRect.bottom + 10
        #job info
        for i in self.description:
            lineSurf = cfg.AR19.render(i, True, cfg.WHITE)
            lineRect = lineSurf.get_rect()
            lineRect.topleft = (jobBackRect.left + 10, y)
            cfg.DISPLAYSURF.blit(lineSurf, lineRect)
            y += 28
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobBackRect.left + 5, jobBackRect.centery),
            (jobBackRect.right - 5, jobBackRect.centery), 1)

        rewardAreaRect = pygame.Rect(jobBackRect.left, jobBackRect.centery, jobBackRect.width, 50)
        jobDetailsRect = pygame.Rect(jobBackRect.left, rewardAreaRect.bottom, jobBackRect.width / 2,
            jobBackRect.height - jobBackRect.height / 2 - rewardAreaRect.height)
        reqDetailsRect = pygame.Rect(jobDetailsRect.right, rewardAreaRect.bottom, jobBackRect.width / 2,
            jobBackRect.height - jobBackRect.height / 2 - rewardAreaRect.height)
        locationAreaRect = pygame.Rect(jobDetailsRect.left, jobDetailsRect.top, jobDetailsRect.width, jobDetailsRect.height / 3)
        timeToCompleteAreaRect = pygame.Rect(jobDetailsRect.left, locationAreaRect.bottom, jobDetailsRect.width, jobDetailsRect.height / 3)
        contactInfoAreaRect = pygame.Rect(jobDetailsRect.left, timeToCompleteAreaRect.bottom, jobDetailsRect.width, jobDetailsRect.height / 3)

        rewardHeaderSurf = cfg.BASICFONT.render('Reward(s): ', True, cfg.WHITE)
        rewardHeaderRect = rewardHeaderSurf.get_rect()
        rewardHeaderRect.midleft = (rewardAreaRect.left + 10, rewardAreaRect.centery)
        cfg.DISPLAYSURF.blit(rewardHeaderSurf, rewardHeaderRect)

        x = rewardHeaderRect.right + 15
        for i, v in self.rewards.items():
            rewardSurf = cfg.AR19.render('-%s %s' % (i, v), True, cfg.WHITE)
            rewardRect = rewardSurf.get_rect()
            rewardRect.midleft = (x, rewardHeaderRect.centery)
            cfg.DISPLAYSURF.blit(rewardSurf, rewardRect)
            x += 150
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobBackRect.left + 5, rewardAreaRect.bottom),
            (jobBackRect.right - 5, rewardAreaRect.bottom), 1)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobDetailsRect.right, jobDetailsRect.top + 5),
            (jobDetailsRect.right, jobDetailsRect.bottom - 5), 1)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobDetailsRect.left + 5, locationAreaRect.bottom),
            (jobDetailsRect.right - 5, locationAreaRect.bottom), 1)
        pygame.draw.line(cfg.DISPLAYSURF, cfg.WHITE, (jobDetailsRect.left + 5, timeToCompleteAreaRect.bottom),
            (jobDetailsRect.right - 5, timeToCompleteAreaRect.bottom), 1)

        locationHeaderSurf = cfg.AR17.render('Location:', True, cfg.WHITE)
        locationHeaderRect = locationHeaderSurf.get_rect()
        locationHeaderRect.midleft = (locationAreaRect.left + 5, locationAreaRect.centery)
        locationSurf = cfg.AR17.render(self.hub, True, cfg.WHITE)
        locationRect = locationSurf.get_rect()
        locationRect.midleft = (locationHeaderRect.right + 10, locationAreaRect.centery)
        cfg.DISPLAYSURF.blit(locationHeaderSurf, locationHeaderRect)
        cfg.DISPLAYSURF.blit(locationSurf, locationRect)

        timeToCompleteHeaderSurf = cfg.AR17.render('Time to complete:', True, cfg.WHITE)
        timeToCompleteHeaderRect = timeToCompleteHeaderSurf.get_rect()
        timeToCompleteHeaderRect.midleft = (timeToCompleteAreaRect.left + 5, timeToCompleteAreaRect.centery)
        timeToCompleteSurf = cfg.AR17.render('%s Days' % self.allowedTime, True, cfg.WHITE)
        timeToCompleteRect = timeToCompleteSurf.get_rect()
        timeToCompleteRect.midleft = (timeToCompleteHeaderRect.right + 10, timeToCompleteAreaRect.centery)
        cfg.DISPLAYSURF.blit(timeToCompleteHeaderSurf, timeToCompleteHeaderRect)
        cfg.DISPLAYSURF.blit(timeToCompleteSurf, timeToCompleteRect)

        contactInfoHeaderSurf = cfg.AR17.render('Contact:', True, cfg.WHITE)
        contactInfoHeaderRect = contactInfoHeaderSurf.get_rect()
        contactInfoHeaderRect.midleft = (contactInfoAreaRect.left + 5, contactInfoAreaRect.centery)
        contactInfoSurf = cfg.AR17.render(self.contact, True, cfg.WHITE)
        contactInfoRect = contactInfoSurf.get_rect()
        contactInfoRect.midleft = (contactInfoHeaderRect.right + 10, contactInfoAreaRect.centery)
        cfg.DISPLAYSURF.blit(contactInfoHeaderSurf, contactInfoHeaderRect)
        cfg.DISPLAYSURF.blit(contactInfoSurf, contactInfoRect)

        reqHeaderSurf = cfg.AR17.render('Suggested Skill Level:', True, cfg.WHITE)
        reqHeaderRect = reqHeaderSurf.get_rect()
        reqHeaderRect.midtop = (reqDetailsRect.centerx, reqDetailsRect.top + 5)
        cfg.DISPLAYSURF.blit(reqHeaderSurf, reqHeaderRect)
        y = reqHeaderRect.bottom + 10
        for i, v in self.reqs.items():
            if v:
                skillSurf = cfg.AR17.render('-%s: %s' % (i, v), True, cfg.WHITE)
            else:
                skillSurf = cfg.AR17.render('-%s' % (i), True, cfg.WHITE)
            skillRect = skillSurf.get_rect()
            skillRect.topleft = (reqDetailsRect.left + 10, y)
            cfg.DISPLAYSURF.blit(skillSurf, skillRect)
            y += 28


        #accept/deny buttons
        acceptBackSurf = pygame.Surface((180, 50))
        acceptBackSurf.fill(cfg.GREEN)
        acceptBackSurf.set_alpha(80)
        acceptBackRect = acceptBackSurf.get_rect()
        acceptBackRect.topleft = (jobBackRect.left + 50, jobBackRect.bottom + 8)
        acceptSurf = cfg.AR25.render('Take Job', True, cfg.WHITE)
        acceptRect = acceptSurf.get_rect()
        acceptRect.center = acceptBackRect.center

        denyBackSurf = pygame.Surface((180, 50))
        denyBackSurf.fill(cfg.RED)
        denyBackSurf.set_alpha(80)
        denyBackRect = denyBackSurf.get_rect()
        denyBackRect.topright = (jobBackRect.right - 50, jobBackRect.bottom + 8)
        denySurf = cfg.AR25.render('Stop Looking', True, cfg.WHITE)
        denyRect = denySurf.get_rect()
        denyRect.center = denyBackRect.center

        if acceptBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            acceptBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Take Job'

        if denyBackRect.collidepoint(cfg.mouseX, cfg.mouseY):
            denyBackSurf.set_alpha(180)
            if cfg.mouseClicked:
                return 'Stop Looking'

        cfg.DISPLAYSURF.blit(acceptBackSurf, acceptBackRect)
        cfg.DISPLAYSURF.blit(acceptSurf, acceptRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, acceptBackRect, 2)
        cfg.DISPLAYSURF.blit(denyBackSurf, denyBackRect)
        cfg.DISPLAYSURF.blit(denySurf, denyRect)
        pygame.draw.rect(cfg.DISPLAYSURF, cfg.WHITE, denyBackRect, 2)




""" --------------------------------- """
