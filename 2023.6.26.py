class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        prefix = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + i
        for i in range(1, n+1):
            if prefix[i] == prefix[n] - prefix[i-1]:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.pivotInteger(n=8))
