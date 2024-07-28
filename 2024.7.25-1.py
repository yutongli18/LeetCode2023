class Solution(object):
    def __init__(self):
        self.matrix = []
        self.m = 0
        self.n = 0
        self.target = 0

    def binary_search(self, start, end):
        """
        二分查找
        :param start: int
        :param end: int
        :return: bool
        """
        if start > end:
            return False
        mid = (start + end) // 2
        x, y = mid // self.n, mid % self.n
        if self.matrix[x][y] == self.target:
            return True
        elif self.matrix[x][y] > self.target:
            return self.binary_search(start, mid - 1)
        else:
            return self.binary_search(mid + 1, end)

    def searchMatrix(self, matrix, target):
        """
        74.搜索二维矩阵
        二分查找
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 初始化
        self.matrix = [[num for num in row] for row in matrix]
        self.m, self.n = len(matrix), len(matrix[0])
        self.target = target
        # 二分查找
        return self.binary_search(0, self.m * self.n - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
