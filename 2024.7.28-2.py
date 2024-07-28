from math import sqrt


class Solution(object):
    def checkPrime(self, num):
        if num == 1:
            return False
        num_factors = 0
        for f in range(1, int(sqrt(num)) + 1):
            if num % f == 0:
                num_factors += 1
            if num_factors > 1:
                return False
        return True

    def nonSpecialCount(self, l, r):
        """
        Q2.统计不是特殊数字的数字数量
        找素数？
        :type l: int
        :type r: int
        :rtype: int
        """
        num_total = r - l + 1
        left = int(sqrt(l))
        if left ** 2 < l:
            left += 1
        right = int(sqrt(r))
        if left > right:
            return num_total
        num_special = 0
        for base in range(left, right + 1):
            if self.checkPrime(base):
                num_special += 1
        return num_total - num_special


if __name__ == "__main__":
    sol = Solution()
    print(sol.nonSpecialCount(4, 16))
