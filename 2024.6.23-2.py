class Solution(object):
    def minimumArea(self, grid):
        """
        100334.包含所有 1 的最小矩形面积 I
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        valid_row, valid_column = [False for _ in range(n)], [False for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    valid_row[j] = True
                    valid_column[i] = True
        width_start, width_end, height_start, height_end = -1, -1, -1, -1
        for i in range(m):
            if valid_column[i]:
                if height_start < 0:
                    height_start = i
                    height_end = height_start
                else:
                    height_end = i
        for j in range(n):
            if valid_row[j]:
                if width_start < 0:
                    width_start = j
                    width_end = width_start
                else:
                    width_end = j
        return (width_end - width_start + 1) * (height_end - height_start + 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumArea(grid=[[0, 1, 0], [1, 0, 1]]))
