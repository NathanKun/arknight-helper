"""
Created on 2018年9月28日

@author: NathanKun
"""

'''
等待 开始行动按钮
循环
    按坐标 任务开始行动按钮
    等待 选择队伍开始行动按钮 或 恢复理智界面
    如果 恢复理智界面
        按坐标 使用至纯源石恢复
        延迟一秒
        按坐标 √按钮
    否则
        按坐标 选择队伍开始行动按钮
        等待 持续监测 接管作战按钮
        等待 行动结束文字
        按坐标 中央
    等待 开始行动按钮
'''


def main():
    refillMax = input('Refill interllect for how much time?\n')
    refillCount = 0
    # check in mission selection interface
    h.waitUntilSelectMission()
    while True:
        h.touchStartMissionA()
        if h.waitSelectTeamOrRefillIntellect() == 'intellect':
            if str(refillCount) == refillMax:
                print('Refill max reached')
                break
            refillCount = refillCount + 1
            print('Refilled ' + str(refillCount) + ' times')
            h.touchRefillIntellect()
            h.wait(1)
            h.touchRefillIntellectConfirm()
            h.wait(3)
        else:
            h.touchStartMissionB()
            h.waitFightStart()
            h.waitFightEnd()
            h.touchFightEnd()
        h.waitUntilSelectMission()


if __name__ == '__main__':
    from log import logger as l

    l.info("Starting...")
    import helper as h
    h.connect()

    l.info("Started")

    main()

    l.info("Stop")
    l.info("-------------------")
    l.info("-------------------")
    l.info("-------------------")
    input()
