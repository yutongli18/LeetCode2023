"""
435. 无重叠区间
贪心：无重叠区间越多，需要删除的区间越少
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        count = 1
        pre_end = intervals[0][1]
        for index in range(1, len(intervals)):
            if intervals[index][0] >= pre_end:
                count += 1
                pre_end = intervals[index][1]
        return len(intervals) - count


if __name__ == '__main__':
    sol = Solution()
    print(sol.eraseOverlapIntervals(
        intervals=[[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98],
                   [-63, 2], [30, 47], [-40, -26]]))
