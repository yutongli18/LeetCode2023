"""
1002.查找共用字符
统计所有字符串所有字符的出现频次，对于每个字符，选择最小的频次作为最终的输出频次。最后，按照频次将字符放到输出列表里。
"""


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a_code = ord('a')
        total_char = [len(words) for _ in range(26)]
        for word in words:
            char = [0 for _ in range(26)]
            for i in range(len(word)):
                char[ord(word[i]) - a_code] += 1
            for i in range(26):
                total_char[i] = min(total_char[i], char[i])
        result = []
        for i in range(26):
            if total_char[i] > 0:
                result.extend([chr(i + a_code)] * total_char[i])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.commonChars(words=["bella", "label", "roller"]))
