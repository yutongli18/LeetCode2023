class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        count = 1
        curr_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curr_end:
                count += 1
                curr_end = intervals[i][1]
        return len(intervals) - count


if __name__ == '__main__':
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
