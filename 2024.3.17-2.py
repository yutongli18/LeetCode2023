"""
100236.统计以给定字符开头和结尾的子字符串总数
"""


class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[i] == c:
                count += 1
        return count + int(count * (count - 1) / 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings(s="abada", c="a"))
