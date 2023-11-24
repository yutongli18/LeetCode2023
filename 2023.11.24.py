"""
738.单调递增的数字
贪心法。
"""


class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bit = []
        rest = n
        while rest > 0:
            n_bit.append(rest % 10)
            rest = int(rest / 10)
        for index in range(len(n_bit) - 1):
            if n_bit[index] < n_bit[index + 1]:
                n_bit[index] = 9
                j = index - 1
                # 需要将之前遍历过的位数都变成9，以保证递增序列
                while j >= 0:
                    n_bit[j] = 9
                    j -= 1
                n_bit[index + 1] -= 1
        print(n_bit)
        new_n = 0
        for index in range(len(n_bit) - 1, -1, -1):
            new_n *= 10
            new_n += n_bit[index]
        return new_n


if __name__ == '__main__':
    sol = Solution()
    print(sol.monotoneIncreasingDigits(n=100))
