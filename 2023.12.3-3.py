"""
100145.统计完全子字符串
一直在超时，思路是正确的了。
"""


from collections import Counter


class Solution(object):
    def countSubStrings(self, word, start, end, k):
        # 返回当前子字符串中的完全子字符串数量
        result = 0
        # 因为只有 26 个英文字母，可以统计
        for m in range(1, 27):
            # 滑动窗口的长度
            l = m * k
            # 如果当前字符串的长度比滑动窗口的长度要短，那么直接结束即可
            if end - start + 1 < l:
                break
            # 初始化滑动窗口
            left, right = start, start + l - 1
            while right <= end:
                counter = Counter(word[left:right+1])
                # 滑动窗口内是完全子字符串
                above_char = 0
                for values in counter.values():
                    if values == k:
                        above_char += 1
                if above_char == m:
                    result += 1
                left += 1
                right += 1
        return result

    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # 完全子字符串
        result = 0
        # 按照 distance <= 2 的条件对字符串进行分组
        # 因为完全子字符串是不可能跨组的
        start, end = 0, 1
        while end < len(word):
            if abs(ord(word[end]) - ord(word[end - 1])) > 2:
                # 计算每一个组中的完全字符串数量
                result += self.countSubStrings(word=word, start=start, end=end - 1, k=k)
                start = end
            end += 1
        result += self.countSubStrings(word=word, start=start, end=end-1, k=k)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countCompleteSubstrings(word="igigee", k=2))
