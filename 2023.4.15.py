"""
1042.不邻接植花
建立邻接矩阵（方便查找），对每一个节点遍历所有的邻接节点，寻找还没有使用过的花的颜色
"""


class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # 邻接矩阵
        adj = [[] for _ in range(n)]
        for path in paths:
            adj[path[0] - 1].append(path[1] - 1)
            adj[path[1] - 1].append(path[0] - 1)
        print(adj)
        answer = [0 for _ in range(n)]
        for i in range(n):
            colored = [False for _ in range(5)]
            # 遍历找哪些颜色已经被使用过
            for vertex in adj[i]:
                colored[answer[vertex]] = True
            for j in range(1, 5):
                if not colored[j]:
                    answer[i] = j
                    break
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.gardenNoAdj(n=4, paths=[[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 1]]))
