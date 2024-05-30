class Solution(object):
    def binary_search(self, matrix, i, start, end, target):
        """
        在 matrix 的行 i 中查找 target
        :param matrix: list[list[int]]
        :param i: int
        :param start: int
        :param end: int
        :param target: int
        :return: bool
        """
        if start > end:
            return False
        mid = (start + end) // 2
        if matrix[i][mid] == target:
            return True
        if matrix[i][mid] > target:
            return self.binary_search(matrix, i, start, mid - 1, target)
        if matrix[i][mid] < target:
            return self.binary_search(matrix, i, mid + 1, end, target)

    def searchMatrix(self, matrix, target):
        """
        240.搜索二维矩阵 II
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        for i in range(m):
            if target < matrix[i][0]:
                # 如果已经比每行的开头要小了，那之后的行都不可能包含 target 了
                break
            if target > matrix[i][n - 1]:
                # 如果比每行的结尾要大，说明不在这一行里，但是下一行也有可能
                continue
            # 行内二分查找
            if self.binary_search(matrix, i, 0, n - 1, target):
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20))
