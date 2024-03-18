"""
100255.成为 K 特殊字符串需要删除的最少字符数
"""
from collections import Counter


class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # 获取字符频数列表
        word_counter = Counter(word)
        freq_list = []
        for _, freq in word_counter.items():
            freq_list.append(freq)
        freq_list.sort()
        # 最少删除字符数
        min_del = len(word)
        for i in range(len(freq_list)):
            curr_del = sum(freq_list[:i]) if i > 0 else 0
            if curr_del >= min_del:
                break
            threshold = freq_list[i] + k
            j = len(freq_list) - 1
            while j >= 0 and freq_list[j] > threshold:
                curr_del += (freq_list[j] - threshold)
                j -= 1
            min_del = min(min_del, curr_del)
        return min_del


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDeletions(word="aaabaaa", k=2))
