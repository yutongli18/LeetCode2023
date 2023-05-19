def before(time1, time2):
    """
    判断time1是否在time2之前
    :param time1: str
    :param time2: str
    :return: bool
    """
    hour1, minute1 = time1.split(":")
    hour2, minute2 = time2.split(":")
    if int(hour1) < int(hour2):
        return True
    elif int(hour1) > int(hour2):
        return False
    else:
        return int(minute1) <= int(minute2)


class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        if before(event1[0], event2[0]):
            return before(event2[0], event1[1])
        else:
            return before(event1[0], event2[1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.haveConflict(event1=["10:00", "11:00"], event2=["14:00", "15:00"]))
