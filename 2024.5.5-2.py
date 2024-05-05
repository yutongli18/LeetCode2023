class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        100275.K 周期字符串需要的最少操作次数
        :type word: str
        :type k: int
        :rtype: int
        """
        # 统计所有 K-字符串的出现频次
        k_counter = {}
        i = 0
        while i < len(word):
            k_counter.setdefault(word[i:i + k], 0)
            k_counter[word[i:i + k]] += 1
            i += k
        # 最少操作次数
        min_ops = len(word) // k + 1
        for splice, count in k_counter.items():
            min_ops = min(min_ops, len(word) // k - count)
        return min_ops


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumOperationsToMakeKPeriodic(word="leetcoleet", k=2))
