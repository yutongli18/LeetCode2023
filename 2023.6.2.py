"""
2559.统计范围内的元音字符串数
直接统计会超出时间限制。
前缀和。
"""


class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        """vowel = ["a", "e", "i", "o", "u"]
        vowelWords = []
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                vowelWords.append(True)
            else:
                vowelWords.append(False)
        result = []
        for query in queries:
            result.append(sum(vowelWords[query[0]:query[1]+1]))
        return result"""
        vowel = ["a", "e", "i", "o", "u"]
        prefixSum = [0]
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                prefixSum.append(prefixSum[-1] + 1)
            else:
                prefixSum.append(prefixSum[-1])
        result = []
        for query in queries:
            result.append(prefixSum[query[1] + 1] - prefixSum[query[0]])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.vowelStrings(words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]))
