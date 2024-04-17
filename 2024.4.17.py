class Solution(object):
    def __init__(self):
        # 皇后计数
        self.n = 0
        # 记录皇后的放置情况
        self.curr_pos = []
        # 方案计数
        self.count = 0

    def backtracking(self, idx):
        """
        第 idx 个皇后应该如何放置
        :type idx: int
        """
        if idx >= self.n:
            # 已经放完了所有的皇后
            self.count += 1
            return
        for pos in range(self.n):
            # 当前测试的位置是：(idx, pos)
            is_valid = True
            for x, y in self.curr_pos:
                # 检查和其它皇后是否能相互攻击
                # 同行同列或同对角线
                if idx == x or pos == y or abs(idx - x) == abs(pos - y):
                    is_valid = False
                    break
            if is_valid:
                # 如果当前位置是有效位置，就放置皇后，递归地摆放下一个皇后
                self.curr_pos.append([idx, pos])
                self.backtracking(idx + 1)
                self.curr_pos.pop()

    def totalNQueens(self, n):
        """
        52. N 皇后 II
        :type n: int
        :rtype: int
        """
        # 初始化
        self.n = n
        # 求解
        self.backtracking(0)
        return self.count


if __name__ == '__main__':
    sol = Solution()
    print(sol.totalNQueens(4))
