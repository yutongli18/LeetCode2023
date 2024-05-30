class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        240.搜索二维矩阵 II
        从右上角开始搜索
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        i, j = 0, n - 1
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20))
