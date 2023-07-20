"""
383.赎金信
哈希表（数组）。
和 242. 有效的字母异位词 类似，但是不需要考虑 ransomNote 能否构成 magazine。
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0 for _ in range(26)]
        for char in magazine:
            counts[ord(char) - ord("a")] += 1
        for char in ransomNote:
            counts[ord(char) - ord("a")] -= 1
        for count in counts:
            if count < 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct(ransomNote="a", magazine="b"))
