"""
977.有序数组的平方
双指针
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsLength = len(nums)
        left, right = 0, numsLength - 1
        stack, resultList = [], []
        while left <= right:
            leftNum, rightNum = nums[left] ** 2, nums[right] ** 2
            if leftNum > rightNum:
                stack.append(leftNum)
                left += 1
            else:
                stack.append(rightNum)
                right -= 1
        while stack:
            resultList.append(stack.pop())
        return resultList


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares(nums=[-4, -1, 0, 3, 10]))
