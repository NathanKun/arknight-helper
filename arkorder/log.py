'''
Created on 2018年9月28日

@author: NathanKun
'''

import logging
logger = logging.getLogger('ark order helper')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('ArkOrderHelper.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def setDebug():
    logger.removeHandler(ch)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)