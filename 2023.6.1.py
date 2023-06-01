"""
2517.礼盒的最大甜蜜度
二分查找+贪心
最小的最大值，一般都是二分查找
"""


def check(price, k, mid):
    prev = 1 - mid
    count = 0
    for p in price:
        if p - prev >= mid:
            count += 1
            prev = p
    return count >= k


class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        left, right = 0, price[-1] - price[0]
        while left < right:
            # print(left, right)
            mid = int((left + right + 1) / 2)
            # print(mid)
            if check(price, k, mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumTastiness(price=[13, 5, 1, 8, 21, 2], k=3))
