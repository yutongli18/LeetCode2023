"""
1262.可被三整除的最大和
动态规划
"""


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for j in range(3):
                # 这个地方可以用一个例子来理解
                # 对于现在的这种输入，当num=5时，
                # num%3=2
                # f[2, 2] = max(f[1, 0]+num, f[1, 2])
                # 换言之，因为j代表的是余数，当选中当前数时，j会发生变化
                g[(j + num % 3) % 3] = max(g[(j + num % 3) % 3], f[j] + num)
            f = g
        return f[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumDivThree(nums=[3, 6, 5, 1, 8]))
