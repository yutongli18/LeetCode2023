"""
1015.可被k整除的最小整数
n不符合64位带符号整数，不能直接用n计算。
考虑直接用余数计算，注意余数的循环关系。
"""


class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        """
        resList = []
        while True:
            if len(resList) == 0:
                res = 1 % k
                if res == 0:
                    break
                resList.append(res)
            newRes = (resList[-1] * 10 + 1) % k
            if newRes == 0:
                break
            if newRes in resList:
                return -1
            resList.append(newRes)
        return len(resList) + 1
        """
        oldRes = 1 % k
        for i in range(1, k+1):
            if oldRes == 0:
                return i
            oldRes = (oldRes * 10 + 1) % k
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestRepunitDivByK(k=2))
