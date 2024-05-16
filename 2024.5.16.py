class Solution(object):
    def trap(self, height):
        """
        42.接雨水
        单调栈
        :type height: List[int]
        :rtype: int
        """
        total_count = 0
        # [height, index]
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and stack[-1][0] <= height[i]:
                # 出现了可以接雨水的凹槽
                mid_height, index = stack.pop(-1)
                if len(stack) > 0:
                    # 凹槽能接雨水的量取决于两边柱子的高度，和两边柱子之间的距离
                    total_count += (min(stack[-1][0], height[i]) - mid_height) * (i - stack[-1][1] - 1)
                # 如果没有前一个柱子，那么这个凹槽没法接雨水
            stack.append([height[i], i])
        return total_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap(height=[4, 2, 0, 3, 2, 5]))
