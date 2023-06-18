"""
1254.统计封闭岛屿的数目
深度优先遍历。
思路是正确的，但是细节上有问题。
每次递归要把所有连通的0都检测出来，而不是碰到边界就返回。
"""


"""def checkClosed(grid, checked, i, j):
    if checked[i][j]:  # 已经检查过
        return False
    checked[i][j] = True
    m, n = len(grid[0]), len(grid)
    if i - 1 < 0 or i + 1 >= n or j - 1 < 0 or j + 1 >= m:  # 至少有一面是边缘，不封闭
        return False
    top = checkClosed(grid, checked, i - 1, j) if grid[i - 1][j] == 0 else True
    left = checkClosed(grid, checked, i, j - 1) if grid[i][j - 1] == 0 else True
    right = checkClosed(grid, checked, i, j + 1) if grid[i][j + 1] == 0 else True
    bottom = checkClosed(grid, checked, i + 1, j) if grid[i + 1][j] == 0 else True
    return top & left & right & bottom"""


def checkedClosed(grid, i, j):
    m, n = len(grid[0]), len(grid)
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if grid[i][j] != 0:
        return True
    grid[i][j] = -1
    top, left, right, bottom = checkedClosed(grid, i - 1, j), \
                               checkedClosed(grid, i, j - 1), \
                               checkedClosed(grid, i, j + 1), \
                               checkedClosed(grid, i + 1, j)
    return top and left and right and bottom



class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m, n = len(grid[0]), len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and checkedClosed(grid, i, j):
                    # print(i, j)
                    count += 1
        print(grid)
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.closedIsland(grid=[[1,1,0,1,1,1,1,1,1,1],
                                 [0,0,1,0,0,1,0,1,1,1],
                                 [1,0,1,0,0,0,1,0,1,0],
                                 [1,1,1,1,1,0,0,1,0,0],
                                 [1,0,1,0,1,1,1,1,1,0],
                                 [0,0,0,0,1,1,0,0,0,0],
                                 [1,0,1,0,0,0,0,1,1,0],
                                 [1,1,0,0,1,1,0,0,0,0],
                                 [0,0,0,1,1,0,1,1,1,0],
                                 [1,1,0,1,0,1,0,0,1,0]]))
