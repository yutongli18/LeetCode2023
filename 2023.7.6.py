"""
59.螺旋矩阵II
模拟。
注意：① 把拐角位置让给下一个循环处理，这样在做每一个外圈的时候，各边上的数字数目是一样多的，可以避开一些复杂的讨论；
② 如何判断每一条边需要填充到什么位置？ 用 n - offset 的方法！不要直接用迭代量叠加！
③ 当 n 为奇数时，需要对中心位置单独处理，正常的填充流程不会填充中心位置。
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(n)] for _ in range(n)]
        startX, startY = 0, 0  # 开始位置
        loop = n // 2  # 迭代次数
        mid = n // 2  # 中心位置
        count = 1  # 记录数字

        for offset in range(1, loop + 1):
            # 先沿着 X 轴从左到右
            for j in range(startY, n - offset):
                result[startX][j] = count
                count += 1
            # 再沿着 Y 轴由上到下
            for i in range(startX, n - offset):
                result[i][n - offset] = count
                count += 1
            # 再沿着 X 轴从右到左
            for j in range(n - offset, startY, -1):
                result[n - offset][j] = count
                count += 1
            # 再沿着 Y 轴从下到上
            for i in range(n - offset, startX, -1):
                result[i][startY] = count
                count += 1
            # 下一个开始位置在对角线上
            startX += 1
            startY += 1
        # 奇数位置填充中心点
        if n % 2 > 0:
            result[mid][mid] = count
        return result
        """result = [[0 for _ in range(n)] for _ in range(n)]

        def makeMatrixLayer(width, start, indexX, indexY):
            # 铺外面一圈
            # width外圈的宽度，start开始的数字，indexX开始的x坐标，indexY开始的y坐标
            # print(width, start, indexX, indexY)
            for _ in range(width):
                # print(indexY, start)
                result[indexX][indexY] = start
                indexY += 1
                start += 1
            indexX += 1
            indexY -= 1
            for _ in range(width - 1):
                # print(indexX, start)
                result[indexX][indexY] = start
                indexX += 1
                start += 1
            indexY -= 1
            indexX -= 1
            for _ in range(width - 1):
                result[indexX][indexY] = start
                indexY -= 1
                start += 1
            indexX -= 1
            indexY += 1
            for _ in range(width - 2):
                result[indexX][indexY] = start
                indexX -= 1
                start += 1
            return start

        preStart = 1
        for i in range(int(n / 2) + 2):
            width = n - 2 * i
            indexX, indexY = i, i
            preStart = makeMatrixLayer(width, preStart, indexX, indexY)
        return result"""


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(n=4))
