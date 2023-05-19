"""
58.最后一个单词的长度
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        words = [word.strip() for word in words]
        i = len(words) - 1
        while i >= 0:
            if words[i] != "":
                return len(words[i])
            i -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord(s="   fly me   to   the moon  "))
