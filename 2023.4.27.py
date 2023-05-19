"""
def preWord(word1, word2):
    word1Length = len(word1)
    word2Length = len(word2)
    if word2Length - word1Length != 1:
        return False
    i, j = 0, 0
    while i < word1Length and j < word2Length and word1[i] == word2[j]:
        i += 1
        j += 1
    if word1[i:] == word2[j+1:]:
        return True
    return False


class Solution(object):
    def longestStrChain(self, words):
        sortedWords = sorted(words, key=lambda x: len(x))
        # print(sortedWords)
        wordsLength = len(sortedWords)
        maxLength = 1
        for i in range(wordsLength):
            j = i + 1
            baseWord = sortedWords[i]
            newLength = 1
            while j < wordsLength:
                # print(baseWord, sortedWords[j])
                if preWord(baseWord, sortedWords[j]):
                    baseWord = sortedWords[j]
                    newLength += 1
                    # print(newLength)
                j += 1
            maxLength = max(maxLength, newLength)
        return maxLength
"""
"""
1048. 最长字符串链
动态规划
对于每一个单词，考虑其可能的最长前序单词链，不要考虑可能对后续带来的影响。
原来的做法是错误的，从前面的单词开始找后面的后续，可能会有多种不同的情况。(a -> ab or a -> ac)
"""


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sortedWords = sorted(words, key=lambda x: len(x))
        lengthDict = {}
        maxLength = 1
        for word in sortedWords:
            lengthDict[word] = 1
            for i in range(len(word)):
                preWord = word[:i] + word[i+1:]
                newLength = lengthDict.get(preWord, 0)
                lengthDict[word] = max(lengthDict[word], newLength+1)
            maxLength = max(maxLength, lengthDict[word])
        return maxLength


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestStrChain(words=["a","ab","ac","bd","abc","abd","abdd"]))
