class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        hourString, minuteString = time.split(":")
        num = 1
        if hourString[0] == "?" and hourString[1] == "?":
            num *= 24
        elif hourString[0] == "?":
            if int(hourString[1]) <= 3:
                num *= 3
            else:
                num *= 2
        elif hourString[1] == "?":
            if hourString[0] == "2":
                num *= 4
            else:
                num *= 10

        if minuteString[0] == "?" and minuteString[1] == "?":
            num *= 60
        elif minuteString[0] == "?":
            num *= 6
        elif minuteString[1] == "?":
            num *= 10

        return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.countTime(time="2?:??"))
