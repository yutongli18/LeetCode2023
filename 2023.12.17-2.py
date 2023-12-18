class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i + 2] - nums[i] > k:
                return []
            else:
                result.append(nums[i:i + 3])
                i += 3
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3))
