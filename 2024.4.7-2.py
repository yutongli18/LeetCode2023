class Solution(object):
    def getSmallestString(self, s, k):
        """
        100242.满足距离约束且字典序最小的字符串
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        # 先统计每个字符换到 a 需要的最小距离
        a_code = ord('a')
        to_a_distance = [0 for _ in range(26)]
        for i in range(1, 26):
            to_a_distance[i] = min(i, 26 - i)
        # 从 s 的最高位开始，如果能换到 a，优先换成 a，否则向左边换
        rest = k
        result_s = ''
        for i in range(len(s)):
            if s[i] == 'a':
                result_s += s[i]
            elif to_a_distance[ord(s[i]) - a_code] <= rest:
                result_s += 'a'
                rest -= to_a_distance[ord(s[i]) - a_code]
            else:
                result_s += chr(ord(s[i]) - rest)
                result_s += s[i+1:]
                break
        return result_s


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSmallestString(s='xaxcd', k=4))
