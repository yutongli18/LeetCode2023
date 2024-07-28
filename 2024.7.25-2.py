class Solution(object):
    def __init__(self):
        self.matrix = []
        self.m = 0
        self.n = 0
        self.target = 0

    def binary_search(self, x, y):
        """
        从右上角开始二分搜索。
        :param x: int
        :param y: int
        :return: bool
        """
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False
        if self.matrix[x][y] == self.target:
            return True
        elif self.matrix[x][y] > self.target:
            return self.binary_search(x, y - 1)
        else:
            return self.binary_search(x + 1, y)

    def searchMatrix(self, matrix, target):
        """
        240.搜索二维矩阵II
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 初始化
        self.matrix = [[num for num in row] for row in matrix]
        self.m, self.n = len(matrix), len(matrix[0])
        self.target = target
        # 二分搜索
        return self.binary_search(0, self.n - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20))
