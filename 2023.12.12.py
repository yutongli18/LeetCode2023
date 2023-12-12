"""
494. 目标和
回溯法：超时。
"""


class Solution(object):
    def __init__(self):
        self.result = 0

    def traverseTarget(self, index, nums, rest):
        if index >= len(nums):
            if rest == 0:
                self.result += 1
            return
        # nums[index] 取负数
        rest -= nums[index] * (-1)
        self.traverseTarget(index=index + 1, nums=nums, rest=rest)
        rest += nums[index] * (-1)
        # nums[index] 取正数
        rest -= nums[index]
        self.traverseTarget(index=index + 1, nums=nums, rest=rest)
        rest += nums[index]
        return

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.traverseTarget(index=0, nums=nums, rest=target)
        return self.result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
