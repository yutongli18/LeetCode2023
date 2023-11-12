class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        nums.sort()
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i, len(nums)):
                y = nums[j]
                if y > 2 * x:
                    break
                max_xor = max(max_xor, x ^ y)
        return max_xor


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumStrongPairXor(nums=[1, 2, 3, 4, 5]))
