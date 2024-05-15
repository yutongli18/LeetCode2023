class Solution(object):
    def threeSum(self, nums):
        """
        15.三数之和
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 结果
        results = []
        nums.sort()
        # 三指针
        left, right = 0, len(nums) - 1
        while left < right < len(nums):
            mid = left + 1
            while mid < right:
                if nums[left] + nums[mid] + nums[right] == 0:
                    if [nums[left], nums[mid], nums[right]] not in results:
                        results.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                elif nums[left] + nums[mid] + nums[right] > 0:
                    right -= 1
                else:
                    mid += 1
            left += 1
            right = len(nums) - 1
        return results


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum(nums=[0, 0, 0]))
