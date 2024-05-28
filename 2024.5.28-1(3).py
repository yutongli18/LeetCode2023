class Solution(object):
    def setZeroes(self, matrix):
        """
        73.矩阵置零
        空间复杂度 O(1)
        用数组的第一行和第一列作为记录数组
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # 因为第一行和第一列要作为记录数组了，所以它们是否包含零的情况需要单独记录
        row_zero, col_zero = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break
        # 遍历矩阵剩下的部分，按照其情况在第一行和第一列上标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    if matrix[i][0] != 0:
                        matrix[i][0] = 0
                    if matrix[0][j] != 0:
                        matrix[0][j] = 0
        # 根据第一行和第一列标记的结果原地修改矩阵的值
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 根据标志位修改第一行和第一列的值
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    sol = Solution()
    sol.setZeroes(matrix=matrix)
    print(matrix)
