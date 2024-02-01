"""
84.柱状图中最大的矩形
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈：从大到小
        stack = []
        # 为了防止错过答案，添加一个首尾边界
        heights.append(0)
        heights.insert(0, 0)
        # 开始遍历
        result = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                mid = stack.pop(-1)
                result = max(result, heights[mid] * (i - stack[-1] - 1))
            stack.append(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
