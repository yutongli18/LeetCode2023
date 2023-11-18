class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_diff, curr_diff = 0, 0
        count = 1
        for index in range(len(nums) - 1):
            curr_diff = nums[index + 1] - nums[index]
            if (pre_diff <= 0 and curr_diff > 0) or (pre_diff >= 0 and curr_diff < 0):
                count += 1
                pre_diff = curr_diff
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.wiggleMaxLength(nums=[1, 7, 4, 9, 2, 5]))
