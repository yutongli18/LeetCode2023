"""
剑指 Offer 58-II.左旋转字符串
Python 简直就是在作弊...
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseLeftWords(s="abcdefg", n=2))
