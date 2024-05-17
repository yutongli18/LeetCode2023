class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        3.无重复字符的最长子串
        :type s: str
        :rtype: int
        """
        max_length = 0
        char_dict = {}
        left, right = 0, 0
        while right < len(s):
            char = s[right]
            char_dict.setdefault(char, 0)
            char_dict[char] += 1
            while char_dict[char] > 1:
                char_dict[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s="pwwkew"))
