import math


class Solution(object):
    def __init__(self):
        self.factors = {}

    def get_factors(self, num, limit):
        """
        求 num 从 limit 开始的全部因子，加入到 self.factors 中
        :param num:
        :param limit:
        :return:
        """
        if num < limit:
            return
        for factor in range(limit, math.isqrt(num) + 1):
            if num % factor == 0:
                self.factors.setdefault(factor, 0)
                self.factors[factor] += 1
                # 为了防止重复
                if factor ** 2 < num:
                    self.factors.setdefault(num // factor, 0)
                    self.factors[num // factor] += 1

    def numberOfPairs(self, nums1, nums2, k):
        """
        100321.优质数对的总数 II
        枚举因子
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        total_count = 0
        limit = min(nums2)
        for num in nums1:
            # 求 nums1 中所有 num 的因子计数
            if num % k != 0:
                continue
            self.get_factors(num // k, limit)
        print(self.factors)
        # 对于 nums2 中的 num，如果是 nums1 的因子，就把对应的计数加上
        for num in nums2:
            if self.factors.get(num):
                total_count += self.factors[num]
        return total_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
