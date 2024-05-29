class Solution(object):
    def rotate(self, matrix):
        """
        48.旋转图像
        直接模拟旋转
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 当前要旋转的位置
        y_bound = n // 2 if n % 2 == 0 else n // 2 + 1
        for i in range(n // 2):
            for j in range(y_bound):
                x, y = i, j
                temp = matrix[x][y]
                while True:
                    temp, matrix[y][n - x - 1] = matrix[y][n - x - 1], temp
                    x, y = y, n - x - 1
                    if x == i and y == j:
                        break


if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol = Solution()
    sol.rotate(matrix=matrix)
    print(matrix)
