class Solution(object):
    def compressedString(self, word):
        """
        100326.压缩字符串 III
        :type word: str
        :rtype: str
        """
        comp = ""
        pre_count = 0
        for i in range(len(word)):
            if i == 0:
                pre_count = 1
                continue
            if word[i] == word[i - 1]:
                pre_count += 1
                if pre_count > 9:
                    comp += ("9" + word[i])
                    pre_count = 1
            else:
                comp += (str(pre_count) + word[i - 1])
                pre_count = 1
        comp += (str(pre_count) + word[-1])
        return comp


if __name__ == "__main__":
    sol = Solution()
    print(sol.compressedString(word="aaaaaaaaaaaaaabb"))
