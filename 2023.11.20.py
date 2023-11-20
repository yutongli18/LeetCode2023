"""
452.用最少数量的箭引爆气球
注意：更新时应该选择最小的右边界，否则出现气球套气球的情况，会多用一支箭。
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count_arrows = 0
        points.sort(key=lambda x: (x[1], x[0]))
        arrow_index = -2 ** 31 - 1
        for index in range(len(points)):
            if points[index][0] <= arrow_index <= points[index][1]:
                continue
            else:
                arrow_index = points[index][1]
                count_arrows += 1
        return count_arrows


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
