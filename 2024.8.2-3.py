class Solution:
    def __init__(self):
        # 最佳方案
        self.best_score = 0
        self.best_path = []
        self.best_rest = []
        # 题目数据
        self.n = 0
        self.m = 0
        self.r = 0
        self.scores = []
        self.heights = []
        self.rest = []
        # DFS用数据
        self.visited = []
        self.curr_score = 0
        self.curr_path = []
        self.curr_rest = []

    def joinPath(self, path, split=""):
        """
        生成用于字典序比较的字符串
        :param path: int[]
        :param split: string
        :return: string
        """
        return split.join([str(aid) for aid in path])

    def dfsPath(self, aid, rest_calc):
        """
        DFS
        :param aid: int
        :param rest_calc: int
        :return: None
        """
        if len(self.curr_path) == self.m:
            # 更新路径
            if self.curr_score > self.best_score:
                self.best_score = self.curr_score
                self.best_path = self.curr_path[:]
                self.best_rest = self.curr_rest[:]
            elif self.curr_score == self.best_score:
                if self.joinPath(self.curr_path) < self.joinPath(self.best_path):
                    self.best_path = self.curr_path[:]
                    self.best_rest = self.curr_rest[:]
                elif self.joinPath(self.curr_path) == self.joinPath(self.best_path):
                    if self.joinPath(self.curr_rest) < self.joinPath(self.best_rest):
                        self.best_rest = self.curr_rest[:]
            return
        # 还可以继续游览
        for nid in range(1, self.n):
            if nid == aid or self.visited[nid] or self.heights[nid] <= self.heights[aid]:
                continue
            self.visited[nid] = True
            self.curr_score += self.scores[nid]
            self.curr_path.append(nid)
            # 考虑在nid是否休息的情况
            if rest_calc == self.r:
                # 必须休息
                if self.rest[nid] == 1:
                    self.curr_rest.append(1)
                    self.dfsPath(nid, 0)
                    self.curr_rest.pop()
            else:
                # 可以休息也可以不休息
                if self.rest[nid] == 1:
                    self.curr_rest.append(1)
                    self.dfsPath(nid, 0)
                    self.curr_rest.pop()
                    self.curr_rest.append(0)
                    self.dfsPath(nid, rest_calc + 1)
                    self.curr_rest.pop()
                else:
                    self.curr_rest.append(0)
                    self.dfsPath(nid, rest_calc + 1)
                    self.curr_rest.pop()
            # 回溯
            self.visited[nid] = False
            self.curr_score -= self.scores[nid]
            self.curr_path.pop()

    def getBestPath(self, n, m, r, scores, heights, rest):
        # 初始化
        # 添加一个虚假的初始景点，它可以到达任何一个景点
        self.n, self.m, self.r = n + 1, m, r
        self.scores, self.heights, self.rest = [0] + scores[:], [-1] + heights[:], [0] + rest[:]
        self.visited = [False for _ in range(self.n)]
        self.visited[0] = True
        # DFS
        self.dfsPath(0, 0)
        print(self.best_score)
        print(self.joinPath(self.best_path, " "))
        print(self.joinPath(self.best_rest, " "))


if __name__ == "__main__":
    sol = Solution()
    sol.getBestPath(5, 3, 2, [10, 5, 12, 8, 15], [2, 1, 4, 3, 5], [0, 1, 0, 1, 0])
