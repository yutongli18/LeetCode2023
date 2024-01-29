"""
503.下一个更大元素 II
遍历 nums 两遍，第一遍赋过值的不重新赋值（但是要入栈，否则会影响结果）。
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [-1 for _ in range(len(nums))]  # 答案
        check = [False for _ in range(len(nums))]  # 已经找到下一个更大元素的值不重新赋值
        stack = []  # 单调栈
        for i in range(len(nums) * 2 - 1):
            curr_index = i if i < len(nums) else i - len(nums)
            while stack and nums[stack[-1]] < nums[curr_index]:
                index = stack.pop(-1)
                if not check[index]:
                    answer[index] = nums[curr_index]
                    check[index] = True
            stack.append(curr_index)
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements(nums=[1, 2, 3, 4, 3]))
