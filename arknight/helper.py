'''
Created on 2018年9月28日

@author: NathanKun
'''

import time
import random

import numpy
import cv2
# import atx # uiautomator1
# pip3 install --pre -U uiautomator2
# install atx-agent on phone: python -m uiautomator2 init
import requests
import uiautomator2 as u2
# from PIL import Image

from log import logger as l

"""
Templates
"""
# templateBadConnection = cv2.imread('templates/bad_connection.jpg')
templateStartMissionA = cv2.imread('templates/mission_select_interface_start_button.jpg')
templateStartMissionA_EVENT = cv2.imread('templates/mission_select_interface_start_button_event.jpg')
templateStartMissionB = cv2.imread('templates/team_select_interface_start_button.jpg')
templateFightingSymbol = cv2.imread('templates/fighting_symbol.jpg')
templateFightEnd = cv2.imread('templates/fight_end_symbol.jpg')
templateNoIntellectSymbol = cv2.imread('templates/no_intellect_symbol.jpg')

"""
Touch Coordinates
"""
# base on 2560x1440
# badConnection_x = 0
# badConnection_y = 0

startMissionA_x = 2650
startMissionA_y = 1300

startMissionB_x = 2360
startMissionB_y = 1020

refillIntellect_x = 2430
refillIntellect_y = 160

refillIntellectConfirm_x = 2340
refillIntellectConfirm_y = 1160

WIFI_IP = '192.168.1.20';

def connect():
    global d
    try:
        d = u2.connect(WIFI_IP)
    except u2.adbutils.errors.AdbError:
        d = u2.connect()


def touchStartMissionA():
    touch(startMissionA_x, startMissionA_y)


def touchStartMissionB():
    touch(startMissionB_x, startMissionB_y)


def touchFightEnd():
    # wait all fight rewards show up
    wait(2)
    touch(1000, 1000)


def touchRefillIntellect():
    touch(refillIntellect_x, refillIntellect_y)


def touchRefillIntellectConfirm():
    touch(refillIntellectConfirm_x, refillIntellectConfirm_y)


def waitUntilSelectMission():
    waitTemplate(templateStartMissionA, 'Entered to select mission interface', template2=templateStartMissionA_EVENT)


def waitFightStart():
    waitTemplate(templateFightingSymbol, 'Start Fighting')


def waitFightEnd():
    waitTemplate(templateFightEnd, 'Fight end')


def waitSelectTeamOrRefillIntellect():
    return waitTemplate(templateStartMissionB, 'Entered to select team or refill intellect interface',
                        template2=templateNoIntellectSymbol, template1Return='team', template2Return='intellect')


'''
def handleBadConnectionPopin(cvImg):
    l.debug('In handleBadConnectionPopin')
    res = cv2.matchTemplate(cvImg, templateBadConnection, cv2.TM_CCOEFF_NORMED)
    
    if cv2.minMaxLoc(res)[1] > 0.925:
        l.info('Bad Connection')
        touch(badConnection_x, badConnection_y)
'''


def waitTemplate(template, log, delay=0.5, precition=0.925, template2=None, template1Return=None, template2Return=None):
    l.debug('In waitTemplateThenTouch')
    tmpt = 0

    while True:
        imgCapt = capture()

        # template1
        res = cv2.matchTemplate(imgCapt, template, cv2.TM_CCOEFF_NORMED)
        if cv2.minMaxLoc(res)[1] > precition:  # check again
            imgCapt = capture()
            res = cv2.matchTemplate(imgCapt, template, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > precition:
                tmpt = 1
                break

        # template2
        if template2 is not None:
            res = cv2.matchTemplate(imgCapt, template2, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res)[1] > precition:  # check again
                imgCapt = capture()
                res = cv2.matchTemplate(imgCapt, template2, cv2.TM_CCOEFF_NORMED)
                if cv2.minMaxLoc(res)[1] > precition:
                    tmpt = 2
                    break

        wait(delay)

    l.info(log)

    if template1Return is not None and template2Return is not None:
        if tmpt == 1:
            return template1Return
        else:
            return template2Return


def capture(savepath=None):
    """
    Take screen snapshot

    Returns:
        PIL.Image object
    """
    global d
    try:
        return d.screenshot(savepath, format='opencv')
    except requests.exceptions.ConnectionError:
        l.info("ConnectionError, try again in 5 sec")
        wait(5)
        connect()
        return capture(savepath, format='opencv')


def wait(sec):
    time.sleep(sec)


def touch(x, y):
    x += random.randrange(-10, 10)
    y += random.randrange(-10, 10)
    d.click(x, y)


'''
def pilToCv2(pilImg):
    return cv2.cvtColor(numpy.array(pilImg), cv2.COLOR_RGB2BGR)
'''


if __name__ == '__main__':
    img = capture('tmp.jpg')
