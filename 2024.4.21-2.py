class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        100291.统计特殊字母的数量 II
        :type word: str
        :rtype: int
        """
        a_code = ord('a')
        A_code = ord('A')
        # 0-未发现，1-发现了而且满足条件，-1-发现了但是不满足条件
        answer = [0 for _ in range(26)]
        exist_list = [[False, False] for _ in range(26)]
        for ch in word:
            # 发现一个大写字母
            if 0 <= ord(ch) - A_code < 26 and answer[ord(ch) - A_code] != -1:
                # 如果前面没有发现过小写字母
                if not exist_list[ord(ch) - A_code][0]:
                    answer[ord(ch) - A_code] = -1
                else:
                    exist_list[ord(ch) - A_code][1] = True
                    answer[ord(ch) - A_code] = 1
            # 发现一个小写字母
            elif 0 <= ord(ch) - a_code < 26 and answer[ord(ch) - a_code] != -1:
                # 如果前面发现过大写字母
                if exist_list[ord(ch) - a_code][1]:
                    answer[ord(ch) - a_code] = -1
                else:
                    exist_list[ord(ch) - a_code][0] = True
        count = 0
        for i in range(26):
            if answer[i] == 1:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSpecialChars(word='abc'))
