"""
131. 分割回文串
回溯法。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_list = []

    def is_palindrome(self, s):
        """
        判断 s 是否为回文串
        :param s: string 待判断的字符串
        :return: bool 是否为回文串
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def get_partition(self, s):
        if not s:
            self.result_list.append(self.curr_list[:])
            return
        for i in range(1, len(s) + 1):
            s_left, s_right = s[:i], s[i:]
            if not self.is_palindrome(s_left):
                continue
            self.curr_list.append(s_left[:])
            self.get_partition(s_right[:])
            self.curr_list.pop(-1)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.get_partition(s[:])
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition(s="a"))
