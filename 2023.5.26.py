"""
1091.二进制矩阵中的最短路径
图上的广度优先遍历，用队列储存所有子节点。
记录到出发点的距离。
如何判断某个节点已经被遍历过是关键。
"""


from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[float("inf")] * n for _ in range(n)]
        dist[0][0] = 1
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1:
                return dist[x][y]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
                        continue
                    if grid[x + dx][y + dy] == 1 or dist[x + dx][y + dy] <= (dist[x][y] + 1):
                        continue
                    dist[x + dx][y + dy] = dist[x][y] + 1
                    queue.append((x + dx, y + dy))
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPathBinaryMatrix(grid=[[1,0,0],[1,1,0],[1,1,0]]))
    # sol.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]])
