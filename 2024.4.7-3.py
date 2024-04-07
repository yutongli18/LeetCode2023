class Solution(object):
    def minOperationsToMakeMedianK(self, nums, k):
        """
        100277.使数组中位数等于 K 的最少操作数
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # 中位数索引
        mid = int(len(nums) / 2)
        # 操作数
        ops = 0
        if nums[mid] == k:
            return ops
        # 中位数左边的值应该小于等于 K
        for i in range(mid):
            if nums[i] > k:
                ops += (nums[i] - k)
        # 中位数右边的值应该大于等于 K
        for i in range(mid + 1, len(nums)):
            if nums[i] < k:
                ops += (k - nums[i])
        # 最后把中位数换一下
        ops += abs(nums[mid] - k)
        return ops


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=4))
