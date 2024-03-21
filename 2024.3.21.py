"""
724.寻找数组的中心下标
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前缀和数组
        pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[i - 1] + nums[i])
        # 判断
        for i in range(len(nums)):
            left_sum = pre_sum[i - 1] if i > 0 else 0
            if left_sum == (pre_sum[-1] - nums[i]) / 2:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.pivotIndex(nums=[-1, -1, -1, -1, -1, -1]))
