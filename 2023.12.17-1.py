class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        checked = [False for _ in range(n * n + 1)]
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if checked[grid[i][j]]:
                    a = grid[i][j]
                else:
                    checked[grid[i][j]] = True
        for i in range(1, n * n + 1):
            if not checked[i]:
                b = i
                break
        return [a, b]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
