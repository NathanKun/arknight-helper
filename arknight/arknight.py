'''
Created on 2018年9月28日

@author: NathanKun
'''

def normalMissionCycle(x, y):
    h.handelMissionSummaryInterface()
    
    h.handelMissionChooseTeamInterface()
    
	# auto search after update 2018-10-18
    #h.handelTouchSearchEnemies()
    
    h.handleFightingLoop()

    h.touch(x, y)

def eventMissionCycle(x, y):
    h.handelEventMissionSummaryInterface()
    
    h.handleFightingLoop()

    h.touch(x, y)

def eventChallengeCycle(challenge):
    h.selectChallengeAndStart(challenge)
    
    h.handleFightingLoop()
    

def main():
    # check in mission selection interface
    missionType = h.waitUntilSelectMission()
    l.info("missionType = " + str(missionType))
    
    if missionType == 1 or missionType == 2:
        # tap mission
        x, y = h.userSelectMission()
    elif missionType == 3:
        challenge = input("Challenge 1, 2 or 3 ?")
    
    while True:
        if missionType == 1:
            normalMissionCycle(x, y)
        elif missionType == 2:
            eventMissionCycle(x, y)
        elif missionType == 3:
            eventChallengeCycle(challenge)

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
