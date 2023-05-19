class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        numsSet = []
        while i < len(nums):
            if nums[i] not in numsSet:
                numsSet.append(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates(nums=[1, 1, 2]))
