"""
100248.字符串及其反转中是否存在同一子字符串
"""


class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            sub_str = ''.join(reversed([s[i], s[i + 1]]))
            if s.find(sub_str) >= 0:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubstringPresent(s="abcd"))
