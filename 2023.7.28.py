"""
28.找出字符串中第一个匹配项的下标
KMP算法
注意：
① 希望在不能匹配回退时，不会回退到开头的位置
② 回退到的位置取决于模式串的匹配前缀和后缀（可以看做模式串在移动）
③ 求前缀和后缀的 getNext 算法，本身也有前进和后退
"""


class Solution(object):
    def getNext(self, needle):
        next = [0 for _ in range(len(needle))]
        j = 0
        next[0] = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:  # 如果不匹配要回退
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j  # 要么回退到 0，彻底不能匹配；要么回退到某个位置，能够匹配
        return next[:]

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        next = self.getNext(needle)
        print(next)
        i, j = 0, 0
        while i < len(haystack):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                # 两种可能：j 回退到 0 之后还是没能和当前的 haystack[i] 达成匹配，此时 j 不动，i 向前一位
                # j = 0 时就不匹配，此时直接向前移动 i 即可
                i += 1
            if j >= len(needle):
                return i - len(needle)
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr(haystack="hello", needle="ll"))
