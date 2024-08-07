class Solution:
    def __init__(self):
        # 最大价值
        self.max_value = 0
        # 初始化
        self.n = 0
        self.m = 0
        self.weights = []
        self.values = []
        self.exclusive = {}
        # DFS遍历用
        self.visited = []
        self.curr_value = 0

    def checkExclusive(self, gid):
        """
        检查当前选择的gid是否和之前选择的商品存在互斥关系
        :param gid: int，商品编号
        :return: bool，是否存在互斥关系
        """
        for sid, value in enumerate(self.visited):
            if value and gid in self.exclusive[sid]:
                return True
        return False

    def dfsGoods(self, gid, rest_m):
        """
        DFS递归所有的商品取法
        :param gid: int，商品编号
        :param rest_m: int，背包剩余容量
        """
        self.max_value = max(self.max_value, self.curr_value)
        for nid in range(1, self.n):
            if nid != gid and not self.visited[nid] and not self.checkExclusive(nid) and rest_m >= self.weights[nid]:
                # 编号为nid的商品可取
                self.visited[nid] = True
                self.curr_value += self.values[nid]
                self.dfsGoods(nid, rest_m - self.weights[nid])
                self.curr_value -= self.values[nid]
                self.visited[nid] = False

    def getMaxValue(self, n, m, k, weights, values, exclusive):
        """
        求最大价值
        :param n: int，商品数量
        :param m: int，背包容量
        :param k: int，互斥关系数量
        :param weights: int[]，商品体积
        :param values: int[]，商品价值
        :param exclusive: {id: int[]}，互斥关系
        :return: int，商品的最大价值
        """
        # 初始化
        self.n, self.m = n + 1, m
        self.weights = [0] + [w for w in weights]
        self.values = [0] + [v for v in values]
        self.exclusive = {gid: ex_list for (gid, ex_list) in exclusive.items()}
        self.visited = [False for _ in range(self.n)]
        # DFS遍历
        self.dfsGoods(0, self.m)
        return self.max_value


if __name__ == "__main__":
    n, m, k = [int(num) for num in input().split(" ")]
    weights, values = [], []
    for _ in range(n):
        w, v = [int(num) for num in input().split(" ")]
        weights.append(w)
        values.append(v)
    exclusive = {}
    for _ in range(k):
        a, b = [int(num) for num in input().split(" ")]
        exclusive.setdefault(a, [])
        exclusive[a].append(b)
        exclusive.setdefault(b, [])
        exclusive[b].append(a)
    sol = Solution()
    print(sol.getMaxValue(n, m, k, weights, values, exclusive))
