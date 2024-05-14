class Solution(object):
    def maxArea(self, height):
        """
        11. 盛最多水的容器
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
