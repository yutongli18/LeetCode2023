"""
100148. 最小数字游戏
"""


class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        left, right = 0, 1
        arr = []
        while right < len(nums):
            arr.append(nums[right])
            arr.append(nums[left])
            left += 2
            right += 2
        return arr


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberGame(nums=[5, 4, 2, 3]))
