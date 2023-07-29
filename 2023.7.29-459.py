"""
459.重复的子字符串
注意：
① KMP 的 next 数组如何得到
② 最长相同前后缀指的是什么？
③ 一点数学推导
"""


class Solution(object):
    def getNext(self, s):
        next_idx = [0 for _ in range(len(s))]
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next_idx[j - 1]
            if s[i] == s[j]:
                j += 1
            next_idx[i] = j
        return next_idx[:]

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        next_idx = self.getNext(s)
        # 这里：如果最后一位的最长相同前后缀长度为 0，说明该字符串不可能由某个子串重复而成
        if next_idx[-1] == 0:
            return False
        # 这里：得到的是重复子串的长度
        re_length = len(s) - next_idx[-1]
        if len(s) % re_length == 0:
            return True
        return False
        """s_length = len(s)
        if s_length <= 1:
            return False
        substr = s[0]
        i, j = 1, 1
        while i < s_length:
            if j >= len(substr) and s[i] != substr[0]:
                substr += s[i]
                i += 1
                j += 1
            elif j < len(substr) and s[i] != substr[j]:
                return False
            elif j < len(substr) and s[i] == substr[j]:
                j += 1
                i += 1
            elif j >= len(substr) and s[i] == substr[0]:  # 这里如果直接返回开头的话，识别不了 abaababaab 这样的字符串
                j = 0
                i += 1
                j += 1
        if j < len(substr):
            return False
        return True"""


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern(s="abaababaab"))
