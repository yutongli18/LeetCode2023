class Solution(object):
    def __init__(self):
        self.results = []  # 所有结果
        self.n = 0
        self.left_num = 0  # 左括号数量
        self.right_num = 0  # 右括号数量
        self.curr = []  # 当前路径

    def trace_back(self):
        if len(self.curr) == self.n * 2:
            self.results.append("".join(self.curr))
        elif self.left_num == self.n:
            self.curr.append(")")
            self.right_num += 1
            self.trace_back()
            self.right_num -= 1
            self.curr.pop()
        elif self.right_num == self.left_num:
            self.curr.append("(")
            self.left_num += 1
            self.trace_back()
            self.left_num -= 1
            self.curr.pop()
        else:
            for char in ["(", ")"]:
                self.curr.append(char)
                if char == "(":
                    self.left_num += 1
                else:
                    self.right_num += 1
                self.trace_back()
                if char == "(":
                    self.left_num -= 1
                else:
                    self.right_num -= 1
                self.curr.pop()

    def generateParenthesis(self, n):
        """
        22.括号生成
        :type n: int
        :rtype: List[str]
        """
        # 初始化
        self.n = n
        # 回溯法
        self.trace_back()
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
