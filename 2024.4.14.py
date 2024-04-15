class Solution(object):
    def findLatestTime(self, s):
        """
        100256.替换字符可以得到的最晚时间
        :type s: str
        :rtype: str
        """
        result = ""
        if s[0] == "?":
            result += "1" if (s[1] == "?" or int(s[1]) <= 1) else "0"
        else:
            result += s[0]
        if s[1] == "?":
            result += "9" if result[0] == "0" else "1"
        else:
            result += s[1]
        result += s[2]
        result += "5" if s[3] == "?" else s[3]
        result += "9" if s[4] == "?" else s[4]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLatestTime(s="1?:?4"))
