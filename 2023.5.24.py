"""
28.找出字符串中第一个匹配项的下标
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr(haystack="sadbutsad", needle="sad"))
