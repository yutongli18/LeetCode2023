class Solution(object):
    def __init__(self):
        self.results = []
        self.n = 0
        self.queue_pos = []

    def trace_back(self, i):
        if i >= self.n:
            curr = []
            for _, y in self.queue_pos:
                curr.append("." * y + "Q" + "." * (self.n - y - 1))
            self.results.append(curr[:])
            return
        for j in range(self.n):
            k = 0
            while k < len(self.queue_pos):
                x, y = self.queue_pos[k]
                if j == y or abs(i - x) == abs(j - y):
                    break
                k += 1
            if k >= len(self.queue_pos):
                self.queue_pos.append([i, j])
                self.trace_back(i + 1)
                self.queue_pos.pop()
        return

    def solveNQueens(self, n):
        """
        51.N皇后
        :type n: int
        :rtype: List[List[str]]
        """
        # 初始化
        self.n = n
        # 回溯法
        self.trace_back(0)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(1))
