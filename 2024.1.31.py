"""
42.接雨水
双指针 / 单调栈
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        # 方法1：双指针
        result = 0
        # 前缀最大值
        pre_max = [height[i] for i in range(len(height))]
        for i in range(1, len(height)):
            pre_max[i] = max(pre_max[i], pre_max[i - 1])
        # 后缀最大值
        post_max = [height[i] for i in range(len(height))]
        for i in range(len(height) - 2, -1, -1):
            post_max[i] = max(post_max[i], post_max[i + 1])
        # 每个柱子顶端接雨水
        for i in range(1, len(height) - 1):  # 第一根柱子和最后一根柱子的顶端不能接雨水
            bound = min(pre_max[i], post_max[i])
            result += (bound - height[i]) if bound > height[i] else 0
        return result
        """
        # 方法2：单调栈
        result = 0
        stack = []  # 单调栈
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:  # 遇到凹坑
                index = stack.pop(-1)
                if stack:  # 没有左边界的凹坑是没法装雨水的
                    bound = min(height[stack[-1]], height[i])  # 凹坑的边缘是当前遍历的元素和单调栈中的上一个元素
                    result += (bound - height[index]) * (i - stack[-1] - 1)  # 能装的雨水是长 * 宽的举行区域
            stack.append(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap(height=[4, 2, 0, 3, 2, 5]))
