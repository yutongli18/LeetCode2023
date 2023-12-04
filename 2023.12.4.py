"""
96. 不同的二叉搜索树
不是二叉树而是二叉搜索树。
二叉搜索树：要求左子树均小于根节点，右子树均大于根节点。
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(n=3))
