"""
56. 合并区间
区间重叠性。
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result_intervals = []
        intervals.sort(key=lambda interval: (interval[0], interval[1]))
        """start, end = intervals[0]
        for index in range(1, len(intervals)):
            if intervals[index][0] > end:
                result_intervals.append([start, end])
                start, end = intervals[index]
            else:
                end = max(end, intervals[index][1])
        result_intervals.append([start, end])
        return result_intervals"""
        # 先把区间加入，再修改右边界，这样可以避开在最后需要单独处理最后一个区间的情况
        result_intervals.append(intervals[0])
        for index in range(1, len(intervals)):
            if intervals[index][0] > result_intervals[-1][1]:
                result_intervals.append(intervals[index])
            else:
                result_intervals[-1][1] = max(result_intervals[-1][1], intervals[index][1])
        return result_intervals


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge(intervals=[[1, 4], [4, 5]]))
