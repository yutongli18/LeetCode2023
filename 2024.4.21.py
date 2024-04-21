class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        100294.统计特殊字母的数量 I
        :type word: str
        :rtype: int
        """
        a_code = ord('a')
        A_code = ord('A')
        exist_list = [[False, False] for _ in range(26)]
        for ch in word:
            if 0 <= ord(ch) - A_code < 26 and not exist_list[ord(ch) - A_code][1]:
                exist_list[ord(ch) - A_code][1] = True
            elif 0 <= ord(ch) - a_code < 26 and not exist_list[ord(ch) - a_code][0]:
                exist_list[ord(ch) - a_code][0] = True
        count = 0
        for i in range(26):
            if exist_list[i][0] and exist_list[i][1]:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSpecialChars(word='aaAbcBC'))
