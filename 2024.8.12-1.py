class Solution:
    def removeArray(self, a, x, k):
        dp = [0 for _ in range(len(a))]
        mex = 0
        visit = set()
        for i in range(len(a) - 1, -1, -1):
            visit.add(a[i])
            while mex in visit:
                mex += 1
            if i < len(a) - 1:
                dp[i] = min(x + dp[i + 1], k * mex)
            else:
                dp[i] = min(x, k * mex)
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        n, k, x = [int(num) for num in input().split(" ")]
        a = [int(num) for num in input().split(" ")]
        print(sol.removeArray(a, k, x))
