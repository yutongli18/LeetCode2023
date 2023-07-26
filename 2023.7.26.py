"""
151.反转字符串中的单词
Python 好像有很多算法都没法向 C 那样实现...
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [word.strip() for word in s.split(" ")]
        # print(words)
        newS = ""
        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                if newS == "":
                    newS += words[i]
                else:
                    newS += (" " + words[i])
        return newS


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords(s="  hello world  "))
    # sol.reverseWords(s="a good   example")
