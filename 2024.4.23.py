class Solution(object):
    def __init__(self):
        # 动态规划数组
        self.dp = []
        # 字符串 s 的长度
        self.s_length = 0
        # 总切割次数
        self.count = 0

    def cut_s(self, start, end):
        """
        分割从 s[start] 到 s[end] 的字符串，使所有子串都为回文串。
        :type start: int
        :type end: int
        :rtype: None
        """
        print(f"({start}, {end})", end="\t")
        if self.dp[start][end] == end - start + 1:
            return
        # 在 s[start:end+1] 的范围内的最长回文子串长度和起止位置
        max_length = 0
        split1, split2 = -1, -1
        for i in range(start, end + 1):
            for j in range(i, end + 1):
                if self.dp[i][j] > max_length:
                    max_length = self.dp[i][j]
                    split1, split2 = i, j
        print(f"({split1}, {split2})", end='\n')
        if split1 == start:
            self.count += 1
            self.cut_s(split2 + 1, end)
        elif split2 == end:
            self.count += 1
            self.cut_s(start, split1 - 1)
        else:
            self.count += 2
            self.cut_s(start, split1 - 1)
            self.cut_s(split2 + 1, end)

    def minCut(self, s):
        """
        132.分割回文串 II
        :type s: str
        :rtype: int
        """
        # 初始化
        self.s_length = len(s)
        self.dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # 动态规划：求以 s[i] 为首，s[j] 为尾的回文串长度
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j]:
                    if i == j:
                        self.dp[i][j] = 1
                    elif i + 1 == j:
                        self.dp[i][j] = 2
                    else:
                        if self.dp[i + 1][j - 1] > 0:
                            self.dp[i][j] = self.dp[i + 1][j - 1] + 2
        # 递归地分割回文串
        self.cut_s(0, self.s_length - 1)
        return self.count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut(
        s="apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
