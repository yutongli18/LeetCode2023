"""
242. 有效的字母异位词
可以直接把字母映射到数组的 26 个位置上去。
遍历第一个字符串时增加，遍历第二个字符串时减小，最后看整个数组的所有位置是否都为 0
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """s_dict, t_dict = {}, {}
        for char in s:
            s_dict.setdefault(char, 0)
            s_dict[char] += 1
        for char in t:
            t_dict.setdefault(char, 0)
            t_dict[char] += 1
        # 判断是否为字母异位词
        if len(s_dict) != len(t_dict):
            return False
        for char in s_dict.keys():
            if s_dict[char] != t_dict.get(char):
                return False
        return True"""
        char_list = [0 for _ in range(26)]
        for char in s:
            char_list[ord(char) - ord("a")] += 1
        for char in t:
            char_list[ord(char) - ord("a")] -= 1
        for num in char_list:
            if num != 0:
                return False
        return True
