class Solution(object):
    def trap(self, height):
        """
        42.接雨水
        双指针
        :type height: List[int]
        :rtype: int
        """
        # 前后缀最大项
        pre_max = [h for h in height]
        post_max = [h for h in height]
        for i in range(1, len(height)):
            pre_max[i] = max(pre_max[i], pre_max[i - 1])
        for i in range(len(height) - 2, -1, -1):
            post_max[i] = max(post_max[i], post_max[i + 1])
        # 雨水量
        total_count = 0
        for i in range(len(height)):
            # 每个柱子顶端能接多少雨水
            # 取决于其左右两边最高的柱子有多高
            total_count += min(pre_max[i], post_max[i]) - height[i]
        return total_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap(height=[4, 2, 0, 3, 2, 5]))
