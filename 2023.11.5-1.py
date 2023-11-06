class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            victory = sum(grid[i])
            if victory == len(grid) - 1:
                return i


if __name__ == '__main__':
    sol = Solution()
    print(sol.findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
