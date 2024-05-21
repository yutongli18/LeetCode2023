class Solution(object):
    def minWindow(self, s, t):
        """
        76.最小覆盖子串
        滑动窗口
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ""
        if len(t) > len(s):
            return result
        # 统计 t 中各个字符的出现频次
        char_set = set()
        char_code_dict = [0 for _ in range(123)]
        for i in range(len(t)):
            char_set.add(t[i])
            char_code_dict[ord(t[i])] += 1
        # 滑动窗口
        left, right = 0, 0
        check_code_dict = [freq for freq in char_code_dict]
        # 尚未覆盖的字符个数
        not_cover = len(char_set)
        while right < len(s):
            # 如果遍历到的字符本身不在 t 中，就不考虑
            if s[right] in char_set:
                check_code_dict[ord(s[right])] -= 1
                # 该字符第一次被全部覆盖
                if check_code_dict[ord(s[right])] == 0:
                    not_cover -= 1
                # 如果当前全部字符都被覆盖到了，移动滑动窗口的左边界，直到刚好不再能够覆盖全部字符为止
                if not_cover <= 0:
                    while left <= right and not_cover <= 0:
                        if s[left] in char_set:
                            check_code_dict[ord(s[left])] += 1
                            if check_code_dict[ord(s[left])] > 0:
                                not_cover += 1
                        left += 1
                    if result == "" or right - left + 2 < len(result):
                        result = s[left - 1:right + 1]
            right += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow(s="aa", t="aa"))
