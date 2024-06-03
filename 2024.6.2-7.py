class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        743.网络延迟时间
        单源最短路径：Bellman-ford 算法。
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        MAX_INT = 10100
        # 构建邻接矩阵
        path = [[MAX_INT for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            path[i][i] = 0
        for [u, v, w] in times:
            path[u][v] = w
        # 从节点 k 到其它所有节点的距离
        k_dist = [path[k][v] for v in range(n + 1)]
        for _ in range(n):
            for [u, v, w] in times:
                if k_dist[v] > k_dist[u] + w:
                    k_dist[v] = k_dist[u] + w
        return max(k_dist[1:]) if max(k_dist[1:]) < MAX_INT else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
