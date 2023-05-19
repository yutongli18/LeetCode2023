class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            return n
        else:
            return 2 * n


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestEvenMultiple(n=10))
