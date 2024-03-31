"""
100263.哈沙德数
"""


class Solution(object):
    def get_bit(self, num):
        rest = num
        bit_list = []
        while rest > 0:
            bit_list.append(rest % 10)
            rest = int(rest / 10)
        return bit_list

    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_list = self.get_bit(x)
        return sum(x_list) if x % sum(x_list) == 0 else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumOfTheDigitsOfHarshadNumber(x=23))
