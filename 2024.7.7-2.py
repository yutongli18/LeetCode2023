class Solution(object):
    def __init__(self):
        self.results = []
        self.candidates = ["0", "1"]
        self.curr_list = []

    def trace_back_valid(self, n):
        if len(self.curr_list) == n:
            self.results.append("".join(self.curr_list))
            return
        for candidate in self.candidates:
            if len(self.curr_list) > 0 and self.curr_list[-1] == "0" and candidate == "0":
                continue
            self.curr_list.append(candidate)
            self.trace_back_valid(n)
            self.curr_list.pop(-1)
        return

    def validStrings(self, n):
        """
        100238.生成不含相邻零的二进制字符串
        回溯？
        :type n: int
        :rtype: List[str]
        """
        self.trace_back_valid(n)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.validStrings(4))
