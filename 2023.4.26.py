"""
1031.两个非重叠子数组的最大和
动态规划+滑动窗口
"""


class Solution(object):
    def help(self, nums, firstLen, secondLen):
        suml = 0
        for i in range(0, firstLen):  # 构造一个长为firstLen的滑动窗口
            suml += nums[i]
        maxSumL = suml  # firstLen子数组和初始值
        sumr = 0
        for i in range(firstLen, firstLen+secondLen):  # 构造一个长为secondLen的滑动窗口（且不重叠）
            sumr += nums[i]
        res = maxSumL + sumr  # secondLen子数组和初始值
        j = firstLen
        for i in range(firstLen+secondLen, len(nums)):
            suml += nums[j] - nums[j-firstLen]
            maxSumL = max(suml, maxSumL)
            sumr += nums[i] - nums[i-secondLen]
            res = max(res, maxSumL+sumr)
            j += 1
        return res

    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        return max(self.help(nums, firstLen, secondLen), self.help(nums, secondLen, firstLen))


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumTwoNoOverlap(nums=[3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen=3, secondLen=2))
