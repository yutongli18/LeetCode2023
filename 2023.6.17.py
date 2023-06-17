"""
2481.分割圆的最少切割次数
"""


class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n % 2 == 0:
            return int(n / 2)
        else:
            return n


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfCuts(n=3))
