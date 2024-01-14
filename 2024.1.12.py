"""
718. 最长重复子数组
和最长公共子序列的区别在于当 nums[i] != nums[j] 时，如何处理 dp 的值。
"""


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 0
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        # 初始化
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
            result = max(result, dp[i][0])
        for j in range(len(nums2)):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
            result = max(result, dp[0][j])
        # 递推公式
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLength(nums1=[1, 2, 3, 2, 8], nums2=[5, 6, 1, 4, 7]))
