class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numsLength = len(nums)
        left, right = 0, numsLength - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            if left > right:
                break
            while right >= left and nums[right] == val:
                right -= 1
            if right < left:
                break
            nums[left], nums[right] = nums[right], nums[left]
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
