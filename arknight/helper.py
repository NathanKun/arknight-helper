'''
Created on 2018年9月28日

@author: NathanKun
'''

import time
import random

import numpy
import cv2
import atx
#from PIL import Image

from ClickableImage import ClickableImage
from log import logger as l


"""
Templates
"""
# bad connection
templateBadConnection = cv2.imread('templates/bad_connection.jpg')
# a icon in select mission interface
templateMissionSelectIcon = cv2.imread('templates/mission_select_icon.jpg')
# a icon in select mission interface for event
templateEventMissionSelectIcon = cv2.imread('templates/mission_select_icon_event.jpg')
# a icon in select mission interface for event
templateEventChallengeStartIcon = cv2.imread('templates/event_challenge_start.jpg')
# choose team button after select mission interface
templateMissionChooseTeam = cv2.imread('templates/mission_choose_team.jpg')
# choose team button after select mission interface
templateEventMissionStart = cv2.imread('templates/event_mission_start.jpg')
# start mission button
templateStartMission = cv2.imread('templates/start_mission.jpg')
# search enemies button
templateSearchEnemiesBtn = cv2.imread('templates/search_enemies_btn.jpg')
# fight button when found enemy
templateFightBtn = cv2.imread('templates/fight_btn.jpg')
# fight end characters after canny
templateFigthEnd = cv2.imread('templates/fight_end.jpg')
# icons in got new card interface
templateNewCard1 = cv2.imread('templates/new_card_got_1.jpg')
templateNewCard2 = cv2.imread('templates/new_card_got_2.jpg')
# choose friend to fight with btn
templateChooseFriendBtn = cv2.imread('templates/choose_friend_fight_btn.jpg')
# request friend btn
templateRequestFriendBtn = cv2.imread('templates/request_friend_btn.jpg')

"""
Touch Coordinates
"""
# base on 2560x1440
badConnection_x = 1525
badConnection_y = 950

chooseTeam_x = 2000
chooseTeam_y = 1150

searchEnemies_x = 2350
searchEnemies_y = 1350

fightBtn_x = 2150
fightBtn_y = 1200

chooseFriendBtn_x = 2370
chooseFriendBtn_y = 340 # friend 1
# chooseFriendBtn_y = 575 # friend 2

closeLockThisCardPopin_x = 1050
closeLockThisCardPopin_y = 910

challengeStart_x = 1260
challengeStart_y = 1200

challenge1_x = 525
challenge1_y = 700

challenge2_x = 1275
challenge2_y = 700

challenge3_x = 2050
challenge3_y = 700

requestFriendBtn_x = 1550
requestFriendBtn_y = 1020


d = atx.connect()


def resizeXY(x, y):
    ratioX = x / 2560
    ratioY = y / 1440
    global badConnection_x
    global badConnection_y
    global chooseTeam_x
    global chooseTeam_y
    global searchEnemies_x
    global searchEnemies_y
    global fightBtn_x
    global fightBtn_y
    global chooseFriendBtn_x
    global chooseFriendBtn_y
    global closeLockThisCardPopin_x
    global closeLockThisCardPopin_y
    global challengeStart_x
    global challengeStart_y
    global challenge1_x
    global challenge1_y
    global challenge2_x
    global challenge2_y
    global challenge3_x
    global challenge3_y
    global requestFriendBtn_x
    global requestFriendBtn_y
    
    badConnection_x = ratioX * badConnection_x
    badConnection_y = ratioY * badConnection_y

    chooseTeam_x = ratioX * chooseTeam_x
    chooseTeam_y = ratioY * chooseTeam_y

    searchEnemies_x = ratioX * searchEnemies_x
    searchEnemies_y = ratioY * searchEnemies_y

    fightBtn_x = ratioX * fightBtn_x
    fightBtn_y = ratioY * fightBtn_y

    chooseFriendBtn_x = ratioX * chooseFriendBtn_x
    chooseFriendBtn_y = ratioY * chooseFriendBtn_y

    closeLockThisCardPopin_x = ratioX * closeLockThisCardPopin_x
    closeLockThisCardPopin_y = ratioY * closeLockThisCardPopin_y

    challengeStart_x = ratioX * challengeStart_x
    challengeStart_y = ratioY * challengeStart_y

    challenge1_x = ratioX * challenge1_x
    challenge1_y = ratioY * challenge1_y

    challenge2_x = ratioX * challenge2_x
    challenge2_y = ratioY * challenge2_y

    challenge3_x = ratioX * challenge3_x
    challenge3_y = ratioY * challenge3_y

    requestFriendBtn_x = ratioX * requestFriendBtn_x
    requestFriendBtn_y = ratioY * requestFriendBtn_y

def selectChallengeAndStart(challenge):
    l.info('Starting Challenge ' + str(challenge))
    if challenge == '1':
        touch(challenge1_x, challenge1_y)
    elif challenge == '2':
        touch(challenge2_x, challenge2_y)
    elif challenge == '3':
        touch(challenge3_x, challenge3_y)
    
    wait(1.5)
    
    touch(challengeStart_x, challengeStart_y)

def waitUntilSelectMission():
    return waitTemplateThenTouch(templateMissionSelectIcon, -1, -1, 'Entered to select mission interface', template2=templateEventMissionSelectIcon, template3=templateEventChallengeStartIcon)


def userSelectMission():
    # let user click
    img = capture()
    
    window = ClickableImage(img)
    mission_x = window.x
    mission_y = window.y
    
    touch(mission_x, mission_y)
    
    wait(1)
    
    # if still in Select Mission Interface, let user click again
    img = capture()
    res = cv2.matchTemplate(pilToCv2(img), templateMissionSelectIcon, cv2.TM_CCOEFF_NORMED)
    if cv2.minMaxLoc(res)[1] > 0.925:
        return userSelectMission()
    else:
        l.info('mission x = ' + str(mission_x) + ", mission y = " + str(mission_y))
        resizeXY(window.screenWidth, window.screenHeight)
        return mission_x, mission_y


def handelMissionSummaryInterface():
    l.debug('In handelMissionSummaryInterface')
    waitTemplateThenTouch(templateMissionChooseTeam, chooseTeam_x, chooseTeam_y, 'Touch choose team')


def handelEventMissionSummaryInterface():
    l.debug('In handelEventMissionSummaryInterface')
    waitTemplateThenTouch(templateEventMissionStart, chooseTeam_x, chooseTeam_y, 'Touch start event')


def handelMissionChooseTeamInterface():
    l.debug('In handelMissionChooseTeamInterface')
    waitTemplateThenTouch(templateStartMission, chooseTeam_x, chooseTeam_y, 'Touch mission start')


def handelTouchSearchEnemies():
    l.debug('In handelTouchSearchEnemies')
    wait(2) # wait for loading
    waitTemplateThenTouch(templateSearchEnemiesBtn, searchEnemies_x, searchEnemies_y, 'Touch auto search enemies')
    
def handleFightingLoop():
    l.debug('In handleFightingLoop')
    # prevent continue touching start fight when no AP
    startFightTouchCount = 0
    
    while True:
        if startFightTouchCount > 10:
            input("No AP")
            startFightTouchCount = 0
        
        img = pilToCv2(capture())
        
        # mission complete ?
        res = cv2.matchTemplate(img, templateMissionSelectIcon, cv2.TM_CCOEFF_NORMED)
        l.debug('mission complete : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            # double check in 1s
            wait(1)
            img = pilToCv2(capture())
            res = cv2.matchTemplate(img, templateMissionSelectIcon, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > 0.925:
                l.info('Mission finished')
                wait(1)
                break;
        
        # event mission complete ?
        res = cv2.matchTemplate(img, templateEventMissionSelectIcon, cv2.TM_CCOEFF_NORMED)
        l.debug('event mission complete : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            # double check in 1s
            wait(1)
            img = pilToCv2(capture())
            res = cv2.matchTemplate(img, templateEventMissionSelectIcon, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > 0.925:
                l.info('Event Mission finished')
                wait(1)
                break;
        
        # event challenge complete ?
        res = cv2.matchTemplate(img, templateEventChallengeStartIcon, cv2.TM_CCOEFF_NORMED)
        l.debug('event challenge complete : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            # double check in 1s
            wait(1)
            img = pilToCv2(capture())
            res = cv2.matchTemplate(img, templateEventChallengeStartIcon, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > 0.925:
                l.info('Event Challenge finished')
                wait(1)
                break;
        
        # found enemy ?
		# auto start after update 2018-10-18
        '''
		res = cv2.matchTemplate(img, templateFightBtn, cv2.TM_CCOEFF_NORMED)
        l.debug('found enemy : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            l.info('Found enemy')
            touch(fightBtn_x, fightBtn_y)
            
            startFightTouchCount += 1
            
            # choose friend to fight with
            wait(2)
            img = pilToCv2(capture())
            res = cv2.matchTemplate(img, templateChooseFriendBtn, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > 0.925:
                l.info('Boss fight')
                touch(chooseFriendBtn_x, chooseFriendBtn_y)
        '''
		
        # got new card ? (check 2 templates)
        res = cv2.matchTemplate(img, templateNewCard1, cv2.TM_CCOEFF_NORMED)
        l.debug('got new card : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            res = cv2.matchTemplate(img, templateNewCard2, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > 0.925:
                l.info('Got new card')
                wait(2) # wait text all shown
                # close possible LockThisCard? pop in
                touch(closeLockThisCardPopin_x, closeLockThisCardPopin_y)
                
                startFightTouchCount = 0
                
        
        # fight end ?
        #img = pilToCv2(img)
        #img = cv2.GaussianBlur(img,(5,5),0) # blur for a better edge detection
        #canny = cv2.Canny(img, 100, 500)    # edge detection
        #canny = Image.fromarray(canny).convert("RGB")
        res = cv2.matchTemplate(img, templateFigthEnd, cv2.TM_CCOEFF_NORMED)
        l.debug('fight end : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            l.info('Fight end')
            touch(fightBtn_x, fightBtn_y)
            wait(3)
            touch(fightBtn_x, fightBtn_y)
                
            startFightTouchCount = 0
                
        
        # request friend popup ?
        res = cv2.matchTemplate(img, templateRequestFriendBtn, cv2.TM_CCOEFF_NORMED)
        l.debug('request friend popup : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > 0.925:
            l.info('Request friend popup')
            touch(requestFriendBtn_x, requestFriendBtn_y)
                
            startFightTouchCount = 0
        
        wait(0.7)
    
    # touch to end


def handleBadConnectionPopin(pilImg):
    l.debug('In handleBadConnectionPopin')
    res = cv2.matchTemplate(pilToCv2(pilImg), templateBadConnection, cv2.TM_CCOEFF_NORMED)
    
    if cv2.minMaxLoc(res)[1] > 0.925:
        l.info('Bad Connection')
        touch(badConnection_x, badConnection_y)


def waitTemplateThenTouch(template, x, y, log, delay=1, precition=0.925, template2=None, template3=None):
    l.debug('In waitTemplateThenTouch')
    found = False
    tplType = -1
    
    while (not found):
        img = capture()
        
        # template1
        res = cv2.matchTemplate(pilToCv2(img), template, cv2.TM_CCOEFF_NORMED)
        l.debug('template1 : ' + str(cv2.minMaxLoc(res)[1]))
        if cv2.minMaxLoc(res)[1] > precition : # check again in 1s
            wait(1)
            img = capture()
            res = cv2.matchTemplate(pilToCv2(img), template, cv2.TM_CCOEFF_NORMED)
            found = cv2.minMaxLoc(res)[1] > precition
            tplType = 1
        
        # template2
        if (template2 is not None):
            res = cv2.matchTemplate(pilToCv2(img), template2, cv2.TM_CCOEFF_NORMED)
            l.debug('template2 : ' + str(cv2.minMaxLoc(res)[1]))
            if cv2.minMaxLoc(res)[1] > precition : # check again in 1s
                wait(1)
                img = capture()
                res = cv2.matchTemplate(pilToCv2(img), template2, cv2.TM_CCOEFF_NORMED)
                found = cv2.minMaxLoc(res)[1] > precition
                tplType = 2
        
        # template3
        if (template3 is not None):
            res = cv2.matchTemplate(pilToCv2(img), template3, cv2.TM_CCOEFF_NORMED)
            l.debug('template2 : ' + str(cv2.minMaxLoc(res)[1]))
            if cv2.minMaxLoc(res)[1] > precition : # check again in 1s
                wait(1)
                img = capture()
                res = cv2.matchTemplate(pilToCv2(img), template3, cv2.TM_CCOEFF_NORMED)
                found = cv2.minMaxLoc(res)[1] > precition
                tplType = 3
            
        wait(delay)
    
    l.info(log)
    
    if (x > 0 and y > 0):
        touch(x, y)
    
    return tplType
        
def connect():
    global d
    d = atx.connect()
    
    
def capture(savepath = None):
    """
    Take screen snapshot

    Returns:
        PIL.Image object
    """
    return d.screenshot(savepath)


def matchColor(image, x, y, r, g, b):
    rgb = image.convert('RGB') # get three R G B values
    ptR, ptG, ptB = rgb.getpixel((x, y))
    l.info(ptR, ptG, ptB)
    
    return ptR == r and ptG == g and ptB == b


def wait(sec):
    time.sleep(sec)


def touch(x, y):
    x += random.randrange(-10, 10)
    y += random.randrange(-10, 10)
    d.touch(x, y)
    
    
def pilToCv2(pilImg):
    return cv2.cvtColor(numpy.array(pilImg), cv2.COLOR_RGB2BGR)
    

if __name__ == '__main__':
    img = capture('tmp.jpg')
    