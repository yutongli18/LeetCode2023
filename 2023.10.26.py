"""
17. 电话号码的字母组合
回溯法，注意此时 curr_index 标识的不是当前 for 循环的开始，而是当前到哪个数字了。
"""


class Solution(object):
    def __init__(self):
        self.digit_char_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                               "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                               "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        self.result_list = []
        self.curr_result = ""

    def getCombines(self, digits, curr_index):
        """
        在当前节点求字母组合。
        我想多了，这里就是单纯的从头开始就行。 "ab" 和 "ba" 算是两种不同的组合。
        :param digits: 包含数字 2 ~ 9 的字符串
        :param curr_index: 当前遍历到的数字索引
        :return: None
        """
        if curr_index == len(digits):
            if self.curr_result:
                self.result_list.append(self.curr_result)
            return
        digit = digits[curr_index]
        char_list = self.digit_char_map[digit]
        for index in range(len(char_list)):
            self.curr_result += char_list[index]
            curr_index += 1
            self.getCombines(digits, curr_index)
            self.curr_result = self.curr_result[:-1]
            curr_index -= 1

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.getCombines(digits, 0)
        return self.result_list
