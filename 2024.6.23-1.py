class Solution(object):
    def minimumAverage(self, nums):
        """
        100342.最小元素和最大元素的最小平均值
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        min_sum = 102
        left, right = 0, len(nums) - 1
        while left < right:
            print(nums[left] + nums[right])
            min_sum = min(min_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        return float(min_sum) / 2


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.minimumAverage(nums=[45, 15, 37, 50, 20, 47, 37, 49, 30, 49, 30, 6, 13, 18, 16, 40, 21, 7, 43, 11, 28, 48]))
