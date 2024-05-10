class Solution(object):
    def twoSum(self, nums, target):
        """
        1.两数之和
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rest_dict = {}
        for i in range(len(nums)):
            if nums[i] in rest_dict.keys():
                return [rest_dict[nums[i]], i]
            rest_dict.setdefault(target - nums[i], i)


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
