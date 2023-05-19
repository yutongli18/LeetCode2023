"""
1017.负二进制转换
用进制转换的方法，当余数为负数时，将其转换为正数，并在除数上加1.
"""


class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        res, remain = n, 0
        result = []
        while res != 0:  # 商可能为负数，不能用res>0作为判断条件
            div = int(res / (-2))
            remain = res - div * (-2)  # 直接用%求余数会得到负数的余数，但是实际上余数可能为正数，例如3%(-2)
            # print(div, remain)
            res = div if remain >= 0 else div + 1
            remain = abs(remain)
            result.append(str(remain))
        result.reverse()
        return "".join(result) if len(result) > 0 else "0"


if __name__ == '__main__':
    sol = Solution()
    print(sol.baseNeg2(n=2))
