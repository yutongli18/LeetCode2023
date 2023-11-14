"""
45. 跳跃游戏 II
贪心或者动态规划。
注意：数组的下标是要到达的地方，数组的值标志着当前下标位置能跳的最远距离。
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """steps = [len(nums) + 1] * len(nums)
        steps[-1] = 0
        for index in range(len(nums) - 2, -1, -1):
            for j in range(index, min(len(nums), index + nums[index] + 1)):
                steps[index] = min(steps[index], 1 + steps[j])
        return steps[0]"""
        if len(nums) == 1:
            return 0
        steps = 0
        curr_cover = 0
        next_cover = 0
        for index in range(len(nums)):
            next_cover = max(next_cover, index + nums[index])
            if index == curr_cover:
                steps += 1
                curr_cover = next_cover
                if next_cover >= len(nums) - 1:
                    break
        return steps


if __name__ == '__main__':
    sol = Solution()
    print(sol.jump(nums=[2, 1]))
