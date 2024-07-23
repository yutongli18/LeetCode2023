class Solution(object):
    def __init__(self):
        self.results = []
        self.s = []
        self.curr = []

    def check(self, start, end):
        """
        检查s是否为回文串。
        :param start: int
        :param end: int
        :return: bool
        """
        left, right = start, end
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True

    def trace_back(self, start):
        """
        回溯
        :param start: int
        :return: None
        """
        for i in range(start, len(self.s)):
            if self.check(start, i):
                self.curr.append("".join(self.s[start:i+1]))
                if i < len(self.s) - 1:
                    self.trace_back(i + 1)
                else:
                    self.results.append(self.curr[:])
                self.curr.pop()

    def partition(self, s):
        """
        131.分割回文串
        :type s: str
        :rtype: List[List[str]]
        """
        # 初始化
        self.s = list(s)
        # 回溯
        self.trace_back(0)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
