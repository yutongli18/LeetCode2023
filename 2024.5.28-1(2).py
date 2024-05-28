class Solution(object):
    def setZeroes(self, matrix):
        """
        73.矩阵置零
        空间复杂度 O(m + n)
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # 统计需要置零的行和列
        zero_rows, zero_cols = [False for _ in range(m)], [False for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if not zero_rows[i]:
                        zero_rows[i] = True
                    if not zero_cols[j]:
                        zero_cols[j] = True
        # 按照统计结果对原矩阵置零
        for i in range(m):
            for j in range(n):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    sol = Solution()
    sol.setZeroes(matrix=matrix)
    print(matrix)
