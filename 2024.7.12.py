from collections import deque


class Solution(object):
    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
        self.visited = []
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def orangesRotting(self, grid):
        """
        994.腐烂的橘子
        不能每个腐烂的橘子各自BFS，因为新鲜橘子被腐烂橘子腐烂的过程是从每个腐烂橘子同时开始的。
        BFS的第一层节点应该是所有的腐烂橘子。
        用一个变量记录新鲜橘子的个数，每次新鲜橘子被腐烂就把个数加1，到最后直接判断这个变量是否等于0即可，不需要再遍历一次。
        BFS
        :type grid: List[List[int]]
        :rtype: int
        """
        time_count = 0
        self.grid = [[num for num in row] for row in grid]
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        queue = deque([])
        # 新鲜橘子的个数
        refresh_count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 2 and not self.visited[i][j]:
                    # 所有的腐烂橘子同时开始腐烂新鲜橘子，因此第一层节点应该是所有的腐烂橘子
                    self.visited[i][j] = True
                    queue.append((i, j))
                if self.grid[i][j] == 1:
                    refresh_count += 1
        while queue:
            # 这层BFS有让新鲜橘子腐烂才有效计数
            is_refresh = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for step_i, step_j in self.steps:
                    new_i, new_j = i + step_i, j + step_j
                    if 0 <= new_i < self.m and 0 <= new_j < self.n \
                            and self.grid[new_i][new_j] != 0 and not self.visited[new_i][new_j]:
                        if self.grid[new_i][new_j] == 1:
                            refresh_count -= 1
                            is_refresh = True
                            self.grid[new_i][new_j] = 2
                        self.visited[new_i][new_j] = True
                        queue.append((new_i, new_j))
            if is_refresh:
                time_count += 1
        return time_count if refresh_count <= 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting(grid=[[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
