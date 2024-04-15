class Solution(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.n = 0

    def get_gcd(self, a, b):
        """
        求 a 和 b 的最大公约数。
        :type a: int
        :type b: int
        :rtype: int
        """
        divisor, rest = a, b
        while True:
            new_rest = divisor % rest
            if new_rest == 0:
                return rest
            divisor = rest
            rest = new_rest

    def binary_search(self, start, end, lcm):
        """
        二分查找，<= mid 的个数有几个
        :type start: int
        :type end: int
        :type lcm: int
        :rtype: int
        """
        # 条件要改，否则会无限循环
        if start >= end:
            return end % (10**9 + 7)
        mid = int((start + end) / 2)
        # 看现在 <= mid 的数有多少个
        count = int(mid / self.a) + int(mid / self.b) - int(mid / lcm)
        # 这里：count = n 也不一定是最小的，还要往左找
        # 因此也不能像是之前做二分查找一样直接抛弃掉 mid 的值，因为它也有可能是答案
        if count >= self.n:
            return self.binary_search(start, mid, lcm)
        else:
            return self.binary_search(mid + 1, end, lcm)

    def nthMagicalNumber(self, n, a, b):
        """
        878. 第 N 个神奇数字
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        self.a, self.b, self.n = a, b, n
        gcd = self.get_gcd(a, b)
        lcm = int(a * b / gcd)
        # 二分查找
        return (self.binary_search(0, min(a, b) * n, lcm)) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthMagicalNumber(n=3, a=6, b=4))
