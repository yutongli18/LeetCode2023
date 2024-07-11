class DisJointSet:
    def __init__(self, length):
        self.fathers = [i for i in range(length)]

    def find(self, x):
        if self.fathers[x] == x:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def join(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.fathers[y] = x


class Solution(object):
    def numIslands(self, grid):
        """
        200.岛屿数量
        并查集
        关键在于什么时候判断当前已经是一座新的岛屿了
        换言之，如果count的初始值是为陆地块的数量，什么时候count应该减1：两个岛屿合并的时候。
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        steps = [[-1, 0], [0, -1]]
        m, n = len(grid), len(grid[0])
        dis_joint_set = DisJointSet(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    idx = i * n + j
                    count += 1
                    for step_i, step_j in steps:
                        if 0 <= i + step_i < m and 0 <= j + step_j < n and grid[i + step_i][j + step_j] == "1":
                            new_idx = (i + step_i) * n + (j + step_j)
                            if not dis_joint_set.is_same(new_idx, idx):
                                dis_joint_set.join(new_idx, idx)
                                count -= 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands(grid=[["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
