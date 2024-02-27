"""
200.岛屿数量
BFS版本解法。
"""


from collections import deque


class Solution(object):
    def __init__(self):
        # 网格
        self.grid = []
        # 边界条件
        self.x_upper = 0
        self.y_upper = 0
        # 移动方向
        self.steps = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # 判断当前位置是否已经遍历过
        self.visited = []

    def bfs_search(self, x, y):
        # 以 (x, y) 为中心标记所有相连的陆地
        queue = deque([(x, y)])
        self.visited[x][y] = True
        while queue:
            pos_x, pos_y = queue.popleft()
            for step in self.steps:
                new_x, new_y = pos_x + step[0], pos_y + step[1]
                if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper and self.grid[new_x][new_y] == "1" \
                        and not self.visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    self.visited[new_x][new_y] = True

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 岛屿个数
        count = 0
        # 初始化
        self.grid = grid
        self.x_upper = len(grid)
        self.y_upper = len(grid[0])
        self.visited = [[False for _ in range(self.y_upper)] for _ in range(self.x_upper)]
        # 开始遍历所有尚未遍历过的陆地
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.grid[i][j] == "1" and not self.visited[i][j]:
                    count += 1
                    # 通过广度优先搜索标记所有与这块陆地相连的陆地，它们构成了一个岛屿
                    self.bfs_search(i, j)
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
