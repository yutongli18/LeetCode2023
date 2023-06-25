"""
1401.圆和矩形是否有重叠
圆心到矩形区域的最短距离和圆的半径比较
"""


class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        dist = 0
        if xCenter < x1 or xCenter > x2:
            dist += min((xCenter - x1) ** 2, (xCenter - x2) ** 2)
        if yCenter < y1 or yCenter > y2:
            dist += min((yCenter - y1) ** 2, (yCenter - y2) ** 2)
        return dist <= radius ** 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkOverlap(radius=1, xCenter=1, yCenter=1, x1=1, y1=-3, x2=2, y2=-1))
