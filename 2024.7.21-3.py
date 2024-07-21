class Solution(object):
    def maxOperations(self, s):
        """
        100360.将1移动到末尾的最大操作次数
        :type s: str
        :rtype: int
        """
        total = 0
        prefix = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                if i < len(s) - 1 and s[i + 1] == "0":
                    prefix += 1
                total += prefix
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxOperations("00111"))
