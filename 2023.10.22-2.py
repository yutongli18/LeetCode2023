"""
100114.元素和最小的山形三元组II
关键：记录前缀和后缀中的最大值和最小值
"""


class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_min = [0 for _ in range(len(nums))]
        post_min = [0 for _ in range(len(nums))]
        pre_min[0] = nums[0]
        post_min[-1] = nums[-1]
        for i in range(1, len(nums)):
            pre_min[i] = min(pre_min[i - 1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            post_min[i] = min(post_min[i + 1], nums[i])

        min_sum = float("inf")
        for i in range(1, len(nums) - 1):
            if nums[i] > max(pre_min[i - 1], post_min[i + 1]):
                min_sum = min(min_sum, nums[i] + pre_min[i - 1] + post_min[i + 1])
        return min_sum if min_sum < float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSum(nums=[8, 6, 1, 5, 3]))
