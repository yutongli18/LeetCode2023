"""
1375.二进制字符串前缀一致的次数
在闭区间[1, i]内的所有位都是1，等价于在前i次翻转中，下标的最大值是i。
"""


class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        count, maxIndex = 0, 0
        n = len(flips)
        for i in range(n):
            maxIndex = max(maxIndex, flips[i] - 1)
            if maxIndex == i:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTimesAllBlue(flips=[3, 2, 4, 1, 5]))
