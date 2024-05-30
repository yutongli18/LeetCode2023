class Solution(object):
    def binary_search(self, matrix, start, end, target):
        if start > end:
            return False
        mid = (start + end) // 2
        i = mid // len(matrix[0])
        j = mid - i * len(matrix[0])
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            return self.binary_search(matrix, start, mid - 1, target)
        else:
            return self.binary_search(matrix, mid + 1, end, target)

    def searchMatrix(self, matrix, target):
        """
        74.搜索二维矩阵
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        return self.binary_search(matrix, 0, len(matrix) * len(matrix[0]) - 1, target)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
