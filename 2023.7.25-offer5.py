"""
剑指 Offer 05.替换空格
双指针（在 Python 上其实区别不大）
"""


import re


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        """s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == " ":
                s_list[i] = "%20"
        return "".join(s_list)"""
        regex = re.compile(r" ")
        return regex.sub("%20", s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceSpace(s="We are happy."))
