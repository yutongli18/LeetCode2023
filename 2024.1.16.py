"""
1035.不相交的线
"""


class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if nums1[i - 1] == nums2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        # 打印 dp 数组
        for i in range(len(nums1) + 1):
            for j in range(len(nums2) + 1):
                print(dp[i][j], end="\t")
            print("\n")
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]))
