"""
29.两数相除
需要把被除数和除数都转换成负数，防止越界。
Z * Y >= X > (Z + 1) * Y，二分法查找Z。
不能用乘法所以用了快速加（但是我没有看懂整个算法的逻辑）
"""


class Solution(object):
    def quickAdd(self, y, z, x):
        result, add = 0, y
        while z > 0:
            if z & 1 == 1:
                if result < x - add:
                    return False
                result += add
            if z != 1:
                if add < x - add:
                    return False
                add += add
            z >>= 1
        return True

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """count = 0
        res = abs(dividend)
        while res >= abs(divisor):
            count += 1
            res -= abs(divisor)
        count = max(-count, -2 ** 31) if dividend * divisor < 0 else min(count, 2 ** 31 - 1)
        return count"""
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            elif divisor == -1:
                return INT_MAX

        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0

        if dividend == 0:
            return 0
        # 把正数转变为负数
        # 在本题中，把负数转变为正数可能会导致超出限制（2 ** 31）
        rev = False
        if dividend > 0:
            dividend *= -1
            rev = not rev
        if divisor > 0:
            divisor *= -1
            rev = not rev
        # 二分查找
        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            check = self.quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # print(ans)
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        return -ans if rev else ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(dividend=100, divisor=7))
