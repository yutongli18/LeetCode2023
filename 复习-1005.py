class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(key=lambda num: abs(num), reverse=True)
        nums_sum = 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
            nums_sum += nums[i]
        while k > 0:
            nums_sum -= nums[-1]
            nums[-1] *= -1
            nums_sum += nums[-1]
            k -= 1
        return nums_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestSumAfterKNegations(nums=[-2, 9, 9, 8, 4], k=5))
