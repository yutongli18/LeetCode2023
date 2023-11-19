class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        count_b = 0
        for index in range(len(s)):
            if s[index] == "1":
                count_b += 1
            if s[index] == "0":
                result += count_b
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSteps(s="00111"))
