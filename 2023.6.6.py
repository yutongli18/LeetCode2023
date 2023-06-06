"""
2352.相等行列对
暴力比较。
"""


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i, j, k = 0, 0, 0
        count = 0
        n = len(grid)
        for i in range(0, n):  # 行
            for j in range(0, n):  # 列
                for k in range(0, n):
                    if grid[i][k] != grid[k][j]:
                        # print(grid[i][k], grid[k][j])
                        break
                if k >= n - 1 and grid[i][k] == grid[k][j]:
                    count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
