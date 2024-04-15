class Solution(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.n = 0
        self.lcms = []

    def get_lcm(self, num1, num2):
        """
        求 num1 和 num2 的最小公倍数。
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # 先求最大公约数
        if num1 < num2:
            num1, num2 = num2, num1
        divisor, rest = num1, num2
        while True:
            temp = divisor % rest
            if temp == 0:
                break
            divisor = rest
            rest = temp
        # 求最小公倍数
        return int(num1 * num2 / rest)

    def binary_search(self, start, end):
        """
        二分搜索。
        :type start: int
        :type end: int
        :rtype: int
        """
        if start >= end:
            return start
        mid = int((start + end) / 2)
        # 计算 <= mid 的，能够被 a 或 b 或 c 整除的数字个数
        count = 0
        for i in range(len(self.lcms)):
            for lcm in self.lcms[i]:
                count += int(mid / lcm * (-1)**i)
        if count >= self.n:
            return self.binary_search(start, mid)
        else:
            return self.binary_search(mid + 1, end)

    def nthUglyNumber(self, n, a, b, c):
        """
        1201.丑数
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        self.a, self.b, self.c, self.n = a, b, c, n
        self.lcms.append([a, b, c])
        self.lcms.append([self.get_lcm(a, b), self.get_lcm(a, c), self.get_lcm(b, c)])
        self.lcms.append([self.get_lcm(self.lcms[1][0], c)])
        return self.binary_search(0, min(a, b, c) * n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(n=3, a=2, b=3, c=5))
