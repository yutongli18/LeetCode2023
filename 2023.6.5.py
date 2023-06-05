"""
2460.对数组执行操作
模拟 + 遍历/双指针
"""


class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        """left, right = 0, n - 1
        while left < right:
            while left < right and nums[left] != 0:
                left += 1
            if left < right:
                while right > left and nums[right] == 0:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]"""
        """newNums = []
        for i in range(0, n - 1):
            if nums[i] > 0:
                newNums.append(nums[i])
        return newNums + [0] * (n - len(newNums))"""
        left, right = 0, 1
        while True:
            while right < n and nums[left] > 0:
                left += 1
                right += 1
            if right < n:
                while right < n and nums[right] == 0:
                    right += 1
                if right < n:
                    nums[left], nums[right] = nums[right], nums[left]
            if right >= n:
                break
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.applyOperations(nums=[847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]))
