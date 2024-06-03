class Solution(object):
    def countDays(self, days, meetings):
        """
        100311.无需开会的工作日
        直接模拟？超时。
        合并无重复区间。
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda item: (item[0], item[1]))
        new_meetings = []
        curr_meetings = meetings[0][:]
        for i in range(1, len(meetings)):
            if meetings[i][0] <= curr_meetings[1]:
                curr_meetings[1] = max(curr_meetings[1], meetings[i][1])
            else:
                new_meetings.append(curr_meetings[:])
                curr_meetings = meetings[i][:]
        new_meetings.append(curr_meetings[:])
        # 用合并后的区间计算需要开会的工作日数
        meeting_count = 0
        for [start, end] in new_meetings:
            meeting_count += (end - start + 1)
        return days - meeting_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]))
