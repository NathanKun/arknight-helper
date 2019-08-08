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

from log import logger as l


"""
Templates
"""
# bad connection
templateBadConnection = cv2.imread('templates/bad_connection.jpg')
# a icon in select mission interface
templateMissionSelectIcon = cv2.imread('templates/mission_select_icon.jpg')
# choose team button after select mission interface
templateMissionChooseTeam = cv2.imread('templates/mission_choose_team.jpg')
# start mission button
templateStartMission = cv2.imread('templates/start_mission.jpg')
# fight end
templateFigthEnd = cv2.imread('templates/fight_end.jpg')
"""
Touch Coordinates
"""
# base on 2560x1440
badConnection_x = 0
badConnection_y = 0

chooseTeam_x = 2000
chooseTeam_y = 1150

fightBtn_x = 2150
fightBtn_y = 1200


d = atx.connect()


def waitUntilSelectMission():
    return waitTemplateThenTouch(templateMissionSelectIcon, -1, -1, 'Entered to select mission interface')


def handelMissionChooseTeamInterface():
    l.debug('In handelMissionChooseTeamInterface')
    waitTemplateThenTouch(templateStartMission, chooseTeam_x, chooseTeam_y, 'Touch mission start')


def handleBadConnectionPopin(pilImg):
    l.debug('In handleBadConnectionPopin')
    res = cv2.matchTemplate(pilToCv2(pilImg), templateBadConnection, cv2.TM_CCOEFF_NORMED)
    
    if cv2.minMaxLoc(res)[1] > 0.925:
        l.info('Bad Connection')
        touch(badConnection_x, badConnection_y)


def waitTemplateThenTouch(template, x, y, log, delay=1, precition=0.925):
    l.debug('In waitTemplateThenTouch')
    found = False
    
    while (not found):
        img = capture()
        
        # template1
        res = cv2.matchTemplate(pilToCv2(img), template, cv2.TM_CCOEFF_NORMED)
        if cv2.minMaxLoc(res)[1] > precition : # check again in 1s
            wait(1)
            img = capture()
            res = cv2.matchTemplate(pilToCv2(img), template, cv2.TM_CCOEFF_NORMED)
            found = cv2.minMaxLoc(res)[1] > precition
        wait(delay)
    
    l.info(log)
    
    if (x > 0 and y > 0):
        touch(x, y)
        
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
    