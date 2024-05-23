class Solution(object):
    def merge(self, intervals):
        """
        56.合并区间
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda interval: [interval[0], interval[1]])
        results = []
        curr_interval = []
        for i in range(len(intervals)):
            if i == 0:
                curr_interval = intervals[i][:]
            if intervals[i][0] > curr_interval[1]:
                results.append(curr_interval[:])
                curr_interval = intervals[i][:]
            else:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
        results.append(curr_interval[:])
        return results


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge(intervals=[[1, 4], [4, 5]]))
