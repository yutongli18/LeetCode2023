class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        统计X和Y频数相等的子矩阵数量
        遍历统计？
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        m, n = len(grid), len(grid[0])
        count = [[[0, 0] for _ in range(n)] for _ in range(m)]
        if grid[0][0] == "X":
            count[0][0][0] += 1
        elif grid[0][0] == "Y":
            count[0][0][1] += 1
        for i in range(1, m):
            count[i][0][0], count[i][0][1] = count[i - 1][0][0], count[i - 1][0][1]
            if grid[i][0] == "X":
                count[i][0][0] += 1
            elif grid[i][0] == "Y":
                count[i][0][1] += 1
            if count[i][0][0] > 0 and count[i][0][0] == count[i][0][1]:
                result += 1
        for j in range(1, n):
            count[0][j][0], count[0][j][1] = count[0][j - 1][0], count[0][j - 1][1]
            if grid[0][j] == "X":
                count[0][j][0] += 1
            elif grid[0][j] == "Y":
                count[0][j][1] += 1
            if count[0][j][0] > 0 and count[0][j][0] == count[0][j][1]:
                result += 1
        for i in range(1, m):
            for j in range(1, n):
                count[i][j][0], count[i][j][1] = count[i - 1][j][0] + count[i][j - 1][0] - count[i - 1][j - 1][0], \
                                                 count[i - 1][j][1] + count[i][j - 1][1] - count[i - 1][j - 1][1]
                if grid[i][j] == "X":
                    count[i][j][0] += 1
                elif grid[i][j] == "Y":
                    count[i][j][1] += 1
                if count[i][j][0] > 0 and count[i][j][0] == count[i][j][1]:
                    result += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubmatrices([[".", ".", "."], ["Y", "X", "."], [".", "X", "."], ["X", "X", "X"]]))
