class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_cover = 0
        index = 0
        while index <= max_cover:
            max_cover = max(max_cover, index + nums[index])
            if max_cover >= len(nums) - 1:
                return True
            index += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump(nums=[3, 2, 1, 0, 4]))
