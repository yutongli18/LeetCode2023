"""
1177.构建回文检测
思路是正确的：成对的字母不需要考虑，只考虑不成对的字母能否在k次替换中替换成对。
用字母本身去判断会超时，可以用二进制位的方法。
"""


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        count = [0 for _ in range(n+1)]
        for i in range(n):
            count[i+1] = count[i] ^ (1 << (ord(s[i]) - ord("a")))  # 前缀和：1表示该位对应的字母只有奇数个
        answer = []
        for left, right, k in queries:
            bits = (count[right+1] ^ count[left]).bit_count()  # 统计为奇数个的字母个数，这些是要通过替换来解决的
            answer.append(bits <= k * 2 + 1)  # k次替换最多能使长度为2k+1的字符串变成回文串
        return answer
        """n = len(queries)
        answer = [False for _ in range(n)]
        for i in range(n):
            left, right, k = queries[i][0], queries[i][1], queries[i][2]
            length = right - left + 1
            count = 0"""
        """    mid = int((left + right) / 2)
            for j in range(left, mid + 1):
                if s[j] != s[left+right-j]:
                    count += 1"""
        """    subCounter = Counter(s[left:right+1])
            for subNum in subCounter.values():
                if subNum % 2 > 0:
                    count += 1
            if length % 2 > 0:
                count -= 1
            count /= 2
            if count <= k:
                answer[i] = True
        return answer"""


if __name__ == '__main__':
    sol = Solution()
    print(sol.canMakePaliQueries(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))
