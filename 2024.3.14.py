"""
1365.有多少小于当前数字的数字
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     nums[i] = (nums[i], i)
        # nums.sort(key=lambda item: item[0])
        # result = [0 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     if nums[i][0] == nums[i - 1][0]:
        #         result[nums[i][1]] = result[nums[i - 1][1]]
        #     else:
        #         result[nums[i][1]] = i
        # return result
        sorted_nums = sorted(nums)
        # 哈希表
        num_smaller = [0 for _ in range(101)]
        for i in range(len(sorted_nums) - 1, -1, -1):
            num_smaller[sorted_nums[i]] = i
        result = []
        for num in nums:
            result.append(num_smaller[num])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
