"""
100228.执行操作使数据元素之和大于等于 K
贪心+枚举
"""


class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        min_steps = k - 1
        # 先增加1再复制，枚举所有增加1的情况：0~k-1
        for i in range(k):
            if k % (1 + i) == 0:
                min_steps = min(min_steps, i + int(k / (1 + i)) - 1)
            else:
                min_steps = min(min_steps, i + int(k / (1 + i)) + 1 - 1)
        return min_steps


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(k=11))
