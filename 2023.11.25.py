class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n + 1)
        f[0] = 0
        if n == 0:
            return f[0]
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(n=2))
