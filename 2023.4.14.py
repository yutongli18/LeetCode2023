import re


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        patternLength = len(pattern)
        queryLength = len(queries)
        answerList = [False for _ in range(queryLength)]
        # patternList = pattern.split()
        # print(patternList)
        regex = "".join([pattern[i] + "[a-z]*" for i in range(patternLength)])
        regex = "^[a-z]*" + regex + "$"
        # print(regex)
        regexObject = re.compile(regex)
        for i in range(queryLength):
            if regexObject.search(queries[i]) is not None:
                answerList[i] = True
        return answerList


if __name__ == '__main__':
    sol = Solution()
    print(sol.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
