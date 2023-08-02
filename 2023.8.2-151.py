"""
151.反转字符串中的单词
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [word.strip() for word in s.split(" ")]
        newS = ""
        for idx in range(len(words) - 1, -1, -1):
            if words[idx] != "":
                if len(newS) > 0:
                    newS += " "
                newS += words[idx]
        return newS


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords(s="   the sky is blue   "))
