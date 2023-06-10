"""
1170.比较字符串最小字母出现频次
"""


from collections import Counter


def function(word):
    """
    求函数 f(word) 的值
    :param word: str
    :return: int
    """
    wordCounter = Counter(word)
    char = min(word)
    return wordCounter.get(char)


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words = [(word, function(word)) for word in words]
        words.sort(key=lambda x: x[1])
        answer = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            queryNum = function(queries[i])
            for j in range(len(words)):
                if words[j][1] > queryNum:
                    answer[i] = len(words) - j
                    break
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSmallerByFrequency(queries=["aabbabbb", "abbbabaa", "aabbbabaa", "aabba", "abb", "a", "ba", "aa", "ba", "baabbbaaaa", "babaa", "bbbbabaa"],
                                    words=["b", "aaaba", "aaaabba", "aa", "aabaabab", "aabbaaabbb", "ababb", "bbb", "aabbbabb", "aab", "bbaaababba", "baaaaa"]))
