class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        if nums[left] > 0 or nums[right] < 0:
            return -1
        while nums[right] > 0:
            while nums[left] < 0 and nums[left] < -nums[right]:
                left += 1
            if nums[left] == -nums[right]:
                return nums[right]
            else:
                right -= 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxK(nums=[-10, 8, 9, 7, -2, -3]))
