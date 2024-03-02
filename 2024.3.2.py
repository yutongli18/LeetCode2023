"""
130.被围绕的区域
DFS BFS
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 矩阵 board
        self.board = []
        self.x_upper = 0
        self.y_upper = 0
        # 移动方向
        self.steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs_solve(self, x, y):
        self.board[x][y] = "A"
        queue = deque([(x, y)])
        while queue:
            pos_x, pos_y = queue.popleft()
            for step in self.steps:
                new_x, new_y = pos_x + step[0], pos_y + step[1]
                if 0 <= new_x < self.x_upper and 0 <= new_y < self.y_upper \
                        and self.board[new_x][new_y] == "O":
                    self.board[new_x][new_y] = "A"
                    queue.append((new_x, new_y))
    # def dfs_solve(self, x, y):
    #     if x < 0 or x >= self.x_upper or y < 0 or y >= self.y_upper \
    #             or self.board[x][y] != "O":
    #         return
    #     self.board[x][y] = "A"
    #     for step in self.steps:
    #         x, y = x + step[0], y + step[1]
    #         self.dfs_solve(x, y)
    #         x, y = x - step[0], y - step[1]
    #     return

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.x_upper = len(board)
        self.y_upper = len(board[0])
        # 先遍历四个边界上的 "O"，把它们修改成无关的 "A"
        for i in range(self.x_upper):
            if self.board[i][0] == "O":
                self.bfs_solve(i, 0)
                # self.dfs_solve(i, 0)
            if self.board[i][self.y_upper - 1] == "O":
                self.bfs_solve(i, self.y_upper - 1)
                # self.dfs_solve(i, self.y_upper - 1)
        for j in range(self.y_upper):
            if self.board[0][j] == "O":
                self.bfs_solve(0, j)
                # self.dfs_solve(0, j)
            if self.board[self.x_upper - 1][j] == "O":
                self.bfs_solve(self.x_upper - 1, j)
                # self.dfs_solve(self.x_upper - 1, j)
        # 再遍历内部的"O"，它们需要被填充
        for i in range(self.x_upper):
            for j in range(self.y_upper):
                if self.board[i][j] == "O":
                    self.board[i][j] = "X"
                elif self.board[i][j] == "A":
                    self.board[i][j] = "O"


if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    sol = Solution()
    sol.solve(board=board)
    print(board)
