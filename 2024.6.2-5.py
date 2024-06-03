import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        743.网络延迟时间
        单源最短路径：Dijkstra 算法
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        MAX_INT = 10100
        # 邻接矩阵
        path = [[MAX_INT for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            path[i][i] = 0
        for [u, v, w] in times:
            path[u][v] = w
        # 从节点 k 到其它节点的距离
        k_dis = [path[k][v] for v in range(n + 1)]
        # 最小堆：记录所有尚未求得最短路径的节点
        min_heap = [(dis, v) for v, dis in enumerate(k_dis)]
        heapq.heapify(min_heap)
        while min_heap:
            dis_mid, mid = heapq.heappop(min_heap)
            # 说明该节点的值已经过时了，后面又更新过或者已经计算完毕了
            if dis_mid > k_dis[mid]:
                continue
            for v in range(1, n + 1):
                if k_dis[v] > dis_mid + path[mid][v]:
                    k_dis[v] = dis_mid + path[mid][v]
                    heapq.heappush(min_heap, (k_dis[v], v))
        return max(k_dis[1:]) if max(k_dis[1:]) < MAX_INT else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times=[[1, 2, 1]], n=2, k=1))
