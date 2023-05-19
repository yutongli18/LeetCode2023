"""
1040.移动石子直到连续II
单纯的分析题。
"""


class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        n = len(stones)
        sortedStones = sorted(stones)
        if sortedStones[n-1] - sortedStones[0] + 1 - n == 0:
            return [0, 0]
        # 最大值为每次移动左端点或右端点到最近的空位
        maxValue = max(sortedStones[n-1] - sortedStones[1] + 1 - (n - 1),
                       sortedStones[n-2] - sortedStones[0] + 1 - (n - 1))
        # 最小值与目前连续的窗口有关
        minValue = n
        j = 0
        for i in range(n):
            while j + 1 < n and sortedStones[j+1] - sortedStones[i] + 1 <= n:
                j += 1
            if j - i + 1 == n - 1 and sortedStones[j] - sortedStones[i] + 1 == n - 1:
                # 窗口右端或左端的棋子距离窗口中最近的棋子的距离为2的情况
                minValue = min(minValue, 2)
                # print("Using this!", i, " ", j)
            else:
                minValue = min(minValue, n - (j - i + 1))
        return [minValue, maxValue]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numMovesStonesII(stones=[1, 2, 3, 4, 7]))
