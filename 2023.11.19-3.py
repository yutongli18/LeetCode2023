"""
100119.最大异或乘积
贪心思想
不知道为什么同样的算法 C++ 能 AC，Python 就不行……
"""


class Solution(object):
    def maximumXorProduct(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        MOD = 1e9 + 7
        ax, bx = (a >> n) << n, (b >> n) << n
        for i in range(n - 1, -1, -1):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            if a_bit == b_bit:
                ax |= 1 << i
                bx |= 1 << i
            else:
                if ax < bx:
                    ax |= 1 << i
                else:
                    bx |= 1 << i
        # 防止乘法运算溢出
        ax = ax % MOD
        bx = bx % MOD
        return int((ax * bx) % MOD)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumXorProduct(a=919266192685640, b=877724646011187, n=11))
