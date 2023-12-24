"""
100156.转换字符串的最小成本 I
我感觉这是个求图上最短路径的题目。
"""


class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        MAX_INT = float("inf")
        # 求最短路径
        path = [[MAX_INT for _ in range(26)] for _ in range(26)]
        for i in range(26):
            path[i][i] = 0
        for i in range(len(original)):
            start = ord(original[i]) - ord("a")
            end = ord(changed[i]) - ord("a")
            # 这里有个细节问题：original 和 changed 里面的字母可以重复
            # “可以重复”的意思不仅仅是指路径可以扩展
            # 还有一种可能是 b -> c 这种直接的路线可以重复多次！
            path[start][end] = min(path[start][end], cost[i])
        # 多源最短路径：Floyd 算法
        for i in range(26):
            # 用第 i 个字母作为中转，考虑从第 j 个字母到第 k 个字母的情况
            for j in range(26):
                for k in range(26):
                    if (path[j][i] + path[i][k]) < path[j][k]:
                        path[j][k] = path[j][i] + path[i][k]
        # 开始考虑字符串的转换
        total_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            total_cost += path[ord(source[i]) - ord("a")][ord(target[i]) - ord("a")]
        return total_cost if total_cost < MAX_INT else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(source="aaaa", target="bbbb", original=["a", "c"],
                          changed=["c", "b"], cost=[1, 2]))
