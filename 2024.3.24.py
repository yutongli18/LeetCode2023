"""
100245.每个字符最多出现两次的最长字符串
滑动窗口。
"""


class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # max_length = 0
        # a_code = ord('a')
        # for i in range(len(s)):
        #     length = 1
        #     char_count = [0 for _ in range(26)]
        #     char_count[ord(s[i]) - a_code] += 1
        #     j = i - 1
        #     while j >= 0 and char_count[ord(s[j]) - a_code] + 1 <= 2:
        #         length += 1
        #         char_count[ord(s[j]) - a_code] += 1
        #         j -= 1
        #     max_length = max(max_length, length)
        # return max_length
        # 滑动窗口
        max_length = 0  # 最长字符串
        start = 0  # 当前滑动窗口的起始位置
        char_count = [0 for _ in range(26)]  # 统计每个字母的出现频率
        a_code = ord('a')  # 字符 a 的 unicode 编码
        for i in range(len(s)):
            char_count[ord(s[i]) - a_code] += 1
            while char_count[ord(s[i]) - a_code] > 2:
                char_count[ord(s[start]) - a_code] -= 1
                start += 1
            max_length = max(max_length, i - start + 1)
        return max_length


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLengthSubstring(s="aaaa"))
