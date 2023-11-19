class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        is_champion = [True] * n
        for edge in edges:
            if is_champion[edge[1]]:
                is_champion[edge[1]] = False
        champion = -1
        for team_id in range(n):
            if is_champion[team_id]:
                if champion < 0:
                    champion = team_id
                else:
                    return -1
        return champion


if __name__ == '__main__':
    sol = Solution()
    print(sol.findChampion(n=3, edges=[[0, 1], [1, 2]]))
