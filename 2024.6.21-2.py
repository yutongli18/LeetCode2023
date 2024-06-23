class Solution:
    def check_sub(self, s, word):
        if len(s) < len(word):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j >= len(word):
            return True
        else:
            return False

    def count_sub(self, s, words):
        count = 0
        for word in words:
            if self.check_sub(s, word):
                count += 1
        return count


if __name__ == '__main__':
    s = input()
    words_str = input()
    words_list = words_str.split(",")
    sol = Solution()
    print(sol.count_sub(s, words_list))
