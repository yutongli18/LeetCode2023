class Solution(object):
    def spiralOrder(self, matrix):
        """
        54.螺旋矩阵
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        traverse_list = []
        is_visited = [[False for _ in range(n)] for _ in range(m)]
        # 开始遍历
        i, j = 0, 0
        i_step, j_step = 0, 1
        while len(traverse_list) < m * n:
            traverse_list.append(matrix[i][j])
            is_visited[i][j] = True
            if i_step == 0:
                # 说明当前是在行上遍历
                if j_step > 0:
                    # 说明当前是在从左向右遍历
                    if j + j_step >= n or is_visited[i][j + j_step]:
                        # 到达右边界，开始向下遍历
                        i_step = 1
                        j_step = 0
                else:
                    # 说明当前是在从右向左遍历
                    if j + j_step < 0 or is_visited[i][j + j_step]:
                        # 到达左边界，开始向上遍历
                        i_step = -1
                        j_step = 0
            else:
                # 说明当前是在列上遍历
                if i_step > 0:
                    if i + i_step >= m or is_visited[i + i_step][j]:
                        # 到达下边界，开始向左遍历
                        i_step = 0
                        j_step = -1
                else:
                    if i + i_step < 0 or is_visited[i + i_step][j]:
                        # 到达上边界，开始向右遍历
                        i_step = 0
                        j_step = 1
            i += i_step
            j += j_step
        return traverse_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
