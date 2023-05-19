"""
2404.出现最频繁的偶数元素
"""


from collections import OrderedDict


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oddDict = OrderedDict()
        sortedNums = sorted(nums)
        for num in sortedNums:
            if num % 2 == 0:
                oddDict.setdefault(num, 0)
                oddDict[num] += 1
        maxKey, maxValue = -1, 0
        for key, value in oddDict.items():
            if value > maxValue:
                maxKey = key
                maxValue = value
        return maxKey


if __name__ == '__main__':
    sol = Solution()
    print(sol.mostFrequentEven(nums=[0, 1, 2, 2, 4, 4, 1]))
