"""
1005.K次取反后最大化的数组和
贪心算法。
"""


class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(key=lambda x: abs(x), reverse=True)
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] *= -1
                k -= 1
                if k == 0:
                    break
        while k > 0:
            nums[-1] *= -1
            k -= 1
        return sum(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2))
