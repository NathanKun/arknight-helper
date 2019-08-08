'''
Created on 2018年9月28日

@author: NathanKun
'''

def main():
    # check in mission selection interface
    h.waitUntilSelectMission()
    while True:
        h.handelSelectMissionInterface()
        h.handelMissionChooseTeamInterface()
        h.handelFight()
        h.waitUntilSelectMission()

if __name__ == '__main__':
    from log import logger as l
    
    l.info("Starting...")
    import helper as h
    
    l.info("Started")
    
    main()
    
    l.info("Stop")
    l.info("-------------------")
    l.info("-------------------")
    l.info("-------------------")
