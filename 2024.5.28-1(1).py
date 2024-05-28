class Solution(object):
    def setZeroes(self, matrix):
        """
        73.矩阵置零
        空间复杂度 O(mn)
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        o_matrix = [[num for num in row] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if o_matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        matrix[k][j] = 0
                    for k in range(len(matrix[0])):
                        matrix[i][k] = 0


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    sol = Solution()
    sol.setZeroes(matrix=matrix)
    print(matrix)
