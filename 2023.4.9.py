class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        charDict = {}
        sLength = len(s)
        for i in range(sLength):
            if s[i] in charDict.keys():
                charDistance = i - charDict[s[i]] - 1
                if charDistance != distance[ord(s[i])-ord("a")]:
                    return False
            else:
                charDict[s[i]] = i
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkDistances(s="aa",
                             distance=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
