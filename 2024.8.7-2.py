from collections import deque


class Solution:
    def getWin(self, n, x, edges):
        # 计算入度
        edge_dict = {}
        in_degree = [0 for _ in range(n + 1)]
        for u, v in edges:
            in_degree[u] += 1
            edge_dict.setdefault(u, [])
            edge_dict[u].append(v)
            in_degree[v] += 1
            edge_dict.setdefault(v, [])
            edge_dict[v].append(u)
        count = 0
        selected = [False for _ in range(n + 1)]
        # 入度为1的节点入队
        queue = deque([])
        for pid in range(1, n + 1):
            if in_degree[pid] == 1:
                if pid == x:
                    return 'xiaoyo'
                queue.append(pid)
        while queue:
            for _ in range(len(queue)):
                pid = queue.popleft()
                count += 1
                selected[pid] = True
                for tid in edge_dict[pid]:
                    if not selected[tid]:
                        in_degree[tid] -= 1
                        if in_degree[tid] == 1:
                            queue.append(tid)
            if selected[x]:
                break
        if not selected[x]:
            return 'Draw'
        if count % 2 == 0:
            return 'Pyrmont'
        return 'Xiaoyo'


if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        n, x = [int(num) for num in input().split(" ")]
        edges = []
        for _ in range(n):
            u, v = [int(num) for num in input().split(" ")]
            edges.append([u, v])
        print(sol.getWin(n, x, edges))
