"""
剑指 Offer 05. 替换空格
Python 没法用双指针法直接求解，只能先转换成列表
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == " ":
                s_list[i] = "%20"
        return "".join(s_list)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceSpace(s="We are happy."))
