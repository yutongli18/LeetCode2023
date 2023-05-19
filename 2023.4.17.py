"""
2409.统计共同度过的日子数
可以把每个日期都转换为每年中的第多少天，然后求区间交集。
"""
mouthDayDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def compareDate(date1, date2):
    # date1 < date2
    if date1[0] < date2[0]:
        return True
    elif (date1[0] == date2[0]) and (date1[1] < date2[1]):
        return True
    return False


def countDays(date1, date2):
    # date2 - date1
    if date1[0] == date2[0]:
        return date2[1] - date1[1] + 1
    days = 0
    for i in range(date1[0]+1, date2[0]):
        days += mouthDayDict[i]
    days += (mouthDayDict[date1[0]] - date1[1] + 1)
    days += date2[1]
    return days


class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        timeList = []
        arriveAliceTime = [int(x) for x in arriveAlice.split("-")]
        leaveAliceTime = [int(x) for x in leaveAlice.split("-")]
        arriveBobTime = [int(x) for x in arriveBob.split("-")]
        leaveBobTime = [int(x) for x in leaveBob.split("-")]
        timeList.append(arriveAliceTime)
        timeList.append(leaveAliceTime)
        timeList.append(arriveBobTime)
        timeList.append(leaveBobTime)
        # print(timeList)

        if compareDate(timeList[1], timeList[2]) or compareDate(timeList[3], timeList[0]):
            return 0

        sortedTimeList = sorted(timeList, key=lambda x: (x[0], x[1]))
        # print(sortedTimeList)
        totalDays = countDays(sortedTimeList[0], sortedTimeList[-1])
        # print(totalDays)

        if compareDate(timeList[0], timeList[2]):
            totalDays -= (countDays(timeList[0], timeList[2]) - 1)
        else:
            totalDays -= (countDays(timeList[2], timeList[0]) - 1)
        if compareDate(timeList[1], timeList[3]):
            totalDays -= (countDays(timeList[1], timeList[3]) - 1)
        else:
            totalDays -= (countDays(timeList[3], timeList[1]) - 1)
        return totalDays


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDaysTogether(arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01", leaveBob="08-19"))
