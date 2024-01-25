"""
739.每日温度
单调栈，只保存下标。
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
