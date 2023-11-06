"""
100116.找到冠军 II
入度为 0 的节点只能有一个。
"""


class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        is_defeated = [False] * n
        for edge in edges:
            if not is_defeated[edge[1]]:
                is_defeated[edge[1]] = True
        if sum(is_defeated) == n - 1:
            for group_id in range(n):
                if not is_defeated[group_id]:
                    return group_id
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findChampion(n=3, edges=[[0, 1], [1, 2]]))
