class Solution(object):
    def spiralOrder(self, matrix):
        """
        54.螺旋矩阵
        按层遍历
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        traverse_list = []
        m, n = len(matrix), len(matrix[0])
        top, left, bottom, right = 0, 0, m - 1, n - 1
        while len(traverse_list) < m * n:
            i, j = top, left
            # 从左向右
            while j <= right:
                traverse_list.append(matrix[i][j])
                j += 1
            # 从上向下
            j -= 1
            i += 1
            while i <= bottom:
                traverse_list.append(matrix[i][j])
                i += 1
            # 从右向左
            i -= 1
            j -= 1
            if top != bottom:
                while j >= left:
                    traverse_list.append(matrix[i][j])
                    j -= 1
            # 从下向上
            j += 1
            i -= 1
            if left != right:
                while i >= top + 1:
                    traverse_list.append(matrix[i][j])
                    i -= 1
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return traverse_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
