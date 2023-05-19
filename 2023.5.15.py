"""
1072.按列翻转得到最大值等行数
没有算法，只有分析。
可能成为等值行的两行之间，要么元素对应相等，要么元素对应相反，只要统计这样的行数，找最大值即可。
可以把每行变成对应的数字来存储，节省空间。
"""


from collections import Counter


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        counter = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                # value是把每一行当做一个n为数字，计算出数字的值，以此来判断两行的对应元素是否相等
                # ^异或运算，当某行首元素为1时将该行所有元素翻转
                value = value * 10 + (matrix[i][j] ^ matrix[i][0])
                # print(value)
            counter[value] += 1
        # print(counter)
        return max(counter.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxEqualRowsAfterFlips(matrix=[[1, 0], [0, 1]]))
