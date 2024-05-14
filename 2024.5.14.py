class Solution(object):
    def moveZeroes(self, nums):
        """
        283.移动零
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        while left < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1
            if left >= len(nums):
                break
            right = left + 1
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right >= len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0]
    sol.moveZeroes(nums=nums)
    print(nums)
