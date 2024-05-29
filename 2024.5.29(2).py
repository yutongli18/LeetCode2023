class Solution(object):
    def rotate(self, matrix):
        """
        48.旋转图像
        先上下翻转，再按照对角线翻转
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先上下翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 再沿着对角线翻转
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    sol.rotate(matrix=matrix)
    print(matrix)
