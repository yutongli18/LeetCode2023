"""
55. 跳跃游戏
能否到达下标位置，数组中存放的是跳跃步数！
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """reachable = [False] * len(nums)
        reachable[0] = True
        for index in range(len(nums)):
            if not reachable[index]:
                continue
            for j in range(index, min(index + nums[index] + 1, len(nums))):
                if not reachable[j]:
                    reachable[j] = True
            if index + nums[index] >= len(nums) - 1:
                return True
        return False"""
        cover = 0
        for index in range(len(nums)):
            if index <= cover:  # 保证当前的 index 位置是可达的
                cover = max(cover, index + nums[index])  # 修正可达位置
                if cover >= len(nums) - 1:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump(nums=[1, 0, 1, 0]))
