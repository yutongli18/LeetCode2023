from collections import deque


class Solution(object):
    def __init__(self):
        self.board = []
        self.m = 0
        self.n = 0
        self.word = ""
        self.step = 0
        self.choices = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.is_visited = []

    def dfs(self, i, j):
        self.step += 1
        self.is_visited[i][j] = True
        if self.step >= len(self.word):
            return True
        for choice_x, choice_y in self.choices:
            x, y = i + choice_x, j + choice_y
            if 0 <= x < self.m and 0 <= y < self.n \
                    and self.board[x][y] == self.word[self.step] and not self.is_visited[x][y]:
                if self.dfs(x, y):
                    return True
        self.step -= 1
        self.is_visited[i][j] = False
        return False

    def exist(self, board, word):
        """
        79.单词搜索
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 初始化
        self.board = [[char for char in row] for row in board]
        self.m, self.n = len(board), len(board[0])
        self.word = word
        self.is_visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        # DFS
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0]:
                    if self.dfs(i, j):
                        return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
