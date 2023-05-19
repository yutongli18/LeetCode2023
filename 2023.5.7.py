"""
1010.总持续时间可被60整除的歌曲
"""


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainders = {}
        timeLength = len(time)
        pairNum = 0
        for i in range(timeLength):
            remainder = time[i] % 60
            # 寻找配对
            if remainder == 0:  # 本身能被60整除的和其它能被60整除的配对，单独考虑
                pairNum += remainders.setdefault(0, 0)
            if remainder > 0 and (60 - remainder in remainders):
                pairNum += remainders[60-remainder]
            # 添加余数
            remainders.setdefault(remainder, 0)
            remainders[remainder] += 1
        return pairNum


if __name__ == '__main__':
    sol = Solution()
    print(sol.numPairsDivisibleBy60(time=[60, 60, 60]))
