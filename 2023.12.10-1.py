class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > count:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3]))
