"""
1043.分隔数组以得到最大和
动态规划。
题解里说是以i为结尾的最大和，但是实际上求解的是(i-k, i-1)这一段的最大和，所以d的长度为n+1。
按照原先的做法，找不到以i为结尾，不分隔的情况。
"""


class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            maxValue = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                d[i] = max(d[i], d[j] + maxValue * (i - j))
                if j > 0:
                    maxValue = max(maxValue, arr[j - 1])
        print(d)
        return d[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
