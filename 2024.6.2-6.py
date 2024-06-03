class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        743.网络延迟时间
        多源最短路径：弗洛伊德算法
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        MAX_INT = 10100
        # 构建路径矩阵
        path = [[MAX_INT for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            path[i][i] = 0
        for [u, v, w] in times:
            path[u][v] = w
        for mid in range(1, n + 1):
            for u in range(1, n + 1):
                if path[u][mid] == MAX_INT:
                    continue
                for v in range(1, n + 1):
                    if path[mid][v] == MAX_INT:
                        continue
                    if path[u][v] > path[u][mid] + path[mid][v]:
                        path[u][v] = path[u][mid] + path[mid][v]
        return max(path[k][1:]) if max(path[k][1:]) < MAX_INT else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(
        times=[[2, 7, 63], [4, 3, 60], [1, 3, 53], [5, 6, 100], [1, 4, 40], [4, 7, 95], [4, 6, 97], [3, 4, 68],
               [1, 7, 75], [2, 6, 84], [1, 6, 27], [5, 3, 25], [6, 2, 2], [3, 7, 57], [5, 4, 2], [7, 1, 53], [5, 7, 35],
               [4, 1, 60], [5, 2, 95], [3, 5, 28], [6, 1, 61], [2, 5, 28]], n=7, k=3))
