"""
LCP33.蓄水
数学问题。
把升级水桶和蓄水操作分开考虑。
"""


import math


class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
        if max(vat) == 0:
            return 0
        count = sum(vat)
        for k in range(1, max(vat) + 1):
            newCount = k
            for j in range(len(vat)):
                newCount += max(0, math.ceil(vat[j] / k) - bucket[j])
            # print(newCount)
            count = min(count, newCount)
            if k >= newCount:
                break
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.storeWater(bucket=[16, 29, 42, 70, 42, 9], vat=[89, 44, 50, 90, 94, 91]))
