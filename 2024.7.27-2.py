class Solution(object):
    def __init__(self):
        self.a_code = ord("a")

    def charCounter(self, s):
        """
        字符统计
        :param s: String
        :return: int[]
        """
        char_dict = [0 for _ in range(26)]
        for i in range(len(s)):
            char_dict[ord(s[i]) - self.a_code] += 1
        return char_dict[:]

    def maxContainsSingle(self, s, a, b):
        """
        一种情况
        先考虑如何满足子串a，再考虑如何满足子串b
        因为顺序和大小写均可调整，所以统计一下字母的个数
        :param s: String
        :param a: String
        :param b: String
        :return: int
        """
        total = 0
        s_counter, a_counter, b_counter = self.charCounter(s), self.charCounter(a.lower()), self.charCounter(b.lower())
        a_max, b_max = len(s) + 1, len(s) + 1
        for i in range(26):
            if a_counter[i] > 0:
                a_max = min(a_max, s_counter[i] // a_counter[i])
        total += a_max
        if a_max > 0:
            for i in range(26):
                if a_counter[i] > 0:
                    s_counter[i] -= a_max * a_counter[i]
        for i in range(26):
            if b_counter[i] > 0:
                b_max = min(b_max, s_counter[i] // b_counter[i])
        total += b_max
        return total

    def maxContains(self, s, a, b):
        """
        程序入口
        :param s: String
        :param a: String
        :param b: String
        :return: int
        """
        if len(a) > len(s) and len(b) > len(s):
            return 0
        return max(self.maxContainsSingle(s, a, b), self.maxContainsSingle(s, b, a))


if __name__ == '__main__':
    s_str = input()
    a_str = input()
    b_str = input()
    sol = Solution()
    print(sol.maxContains(s_str, a_str, b_str))
