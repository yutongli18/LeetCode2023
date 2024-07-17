class Solution(object):
    def __init__(self):
        self.char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.digits = []
        self.curr_path = []
        self.results = []

    def trace_back(self, i):
        for char in self.char_map[self.digits[i]]:
            self.curr_path.append(char)
            if len(self.curr_path) >= len(self.digits):
                self.results.append("".join(self.curr_path))
            else:
                self.trace_back(i + 1)
            self.curr_path.pop()

    def letterCombinations(self, digits):
        """
        17.电话号码的字母组合
        :type digits: str
        :rtype: List[str]
        """
        self.digits = list(digits)
        if len(self.digits) <= 0:
            return self.results
        self.trace_back(0)
        return self.results


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(digits="2"))
