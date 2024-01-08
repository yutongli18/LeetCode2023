"""
2976.转换字符串的最小成本 I
"""


class Solution(object):
    def __init__(self):
        # 问题1：关于不可达的设置。
        # 这里不能简单的用 10 ** 6 + 1 作为不可达的指标，因为正常的通路也有可能超过这个距离。
        self.MAX_DIS = -1
        self.base = ord("a")
        self.distance_matrix = [[self.MAX_DIS for _ in range(26)] for _ in range(26)]
        # 相同节点的距离为 0
        for i in range(26):
            self.distance_matrix[i][i] = 0

    def get_distance_matrix(self, original, changed, cost):
        # 初始化矩阵
        for i in range(len(original)):
            s, t = original[i], changed[i]
            curr_distance = self.distance_matrix[ord(s) - self.base][ord(t) - self.base]
            # 问题2：关于不可达的特殊处理。
            # 每次在赋值时都要考虑原来是不是不可达状态，因为选定的标志距离是 -1。
            if curr_distance == self.MAX_DIS:
                # 从不可达变成可达状态
                self.distance_matrix[ord(s) - self.base][ord(t) - self.base] = cost[i]
            else:
                # 选取最短的路径
                self.distance_matrix[ord(s) - self.base][ord(t) - self.base] = min(
                    self.distance_matrix[ord(s) - self.base][ord(t) - self.base], cost[i])
        # Floyd 算法
        for i in range(26):
            # 以字母序号为 i 的节点作为中间点
            for j in range(26):
                for k in range(26):
                    if self.distance_matrix[j][i] == self.MAX_DIS or self.distance_matrix[i][k] == self.MAX_DIS:
                        # 如果有任意一段不可达，那么整体就不可达
                        continue
                    new_distance = self.distance_matrix[j][i] + self.distance_matrix[i][k]
                    # 这里也是不可达的特殊处理。
                    if self.distance_matrix[j][k] == self.MAX_DIS:
                        self.distance_matrix[j][k] = new_distance
                    else:
                        self.distance_matrix[j][k] = min(self.distance_matrix[j][k], new_distance)

    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        self.get_distance_matrix(original=original, changed=changed, cost=cost)
        total_cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                curr_cost = self.distance_matrix[ord(source[i]) - self.base][ord(target[i]) - self.base]
                # 问题3：如果不可达，直接返回 -1，无需继续计算。
                if curr_cost == -1:
                    # 如果不可达，那么表示不可转换
                    return -1
                else:
                    total_cost += curr_cost
        return total_cost


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(source="aaaa", target="bbbb", original=["a", "c"],
                          changed=["c", "b"], cost=[1, 2]))
