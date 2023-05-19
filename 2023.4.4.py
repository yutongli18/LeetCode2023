"""
17.电话号码的字母组合
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numCharDict = {"2": ["a", "b", "c"],
                       "3": ["d", "e", "f"],
                       "4": ["g", "h", "i"],
                       "5": ["j", "k", "l"],
                       "6": ["m", "n", "o"],
                       "7": ["p", "q", "r", "s"],
                       "8": ["t", "u", "v"],
                       "9": ["w", "x", "y", "z"]}
        resultList = []
        for digit in digits:
            if len(resultList) == 0:
                resultList = numCharDict[digit]
            else:
                newList = []
                for result in resultList:
                    for char in numCharDict[digit]:
                        newList.append(result + char)
                resultList = newList[:]
        return resultList


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations(digits="23"))
