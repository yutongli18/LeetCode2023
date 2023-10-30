"""
100111. 找出数组中的 K-or 值
"""


class Solution(object):
    def __init__(self):
        # nums 中每个 num 各位中 1 的个数之和
        # 这个个数之和如果能超过 k，说明该位的值是 1
        self.bit_count = {}

    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_index = 0
        for num in nums:
            num_bit = bin(num)
            max_index = max(max_index, len(num_bit) - 3)
            for i in range(2, len(num_bit)):
                self.bit_count.setdefault(len(num_bit) - 1 - i, 0)
                if num_bit[i] == "1":
                    self.bit_count[len(num_bit) - 1 - i] += 1
        k_for = 0
        for index in range(0, max_index + 1):
            if self.bit_count[index] >= k:
                k_for += 2 ** index
        return k_for


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKOr(nums=[10, 8, 5, 9, 11, 6, 8], k=1))
