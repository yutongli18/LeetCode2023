class Solution(object):
    def __init__(self):
        self.coins = []
        self.k = 0
        self.m = 0
        self.lcms = []
        # DFS 求 lcms 用
        self.curr_group = []

    def get_lcm(self, a, b):
        """
        求 a 和 b 的最小公倍数。
        :type a: int
        :type b: int
        :rtype: int
        """
        # 先求最大公约数
        # 辗转相除法
        divisor, rest = a, b
        while True:
            new_rest = divisor % rest
            if new_rest == 0:
                break
            divisor = rest
            rest = new_rest
        # 根据最大公约数求最小公倍数
        return int(a * b / rest)

    def backtracking(self, start):
        if start >= len(self.coins):
            return
        for i in range(start, len(self.coins)):
            self.curr_group.append(i)
            level = len(self.curr_group) - 1
            if level == 0:
                self.lcms[level].append(self.coins[i])
            else:
                self.lcms[level].append(self.get_lcm(self.lcms[level-1][-1], self.coins[i]))
            self.backtracking(i + 1)
            self.curr_group.pop()
        return

    def binary_search(self, start, end):
        """
        二分搜索。
        :type start: int
        :type end: int
        :rtype: int
        """
        if start >= end:
            return start
        mid = int((start + end) / 2)
        # 计算当前 <= mid，能被 coins 整除的数字个数
        count = 0
        for i in range(len(self.lcms)):
            for lcm in self.lcms[i]:
                count += int(mid / lcm * (-1) ** i)
        # 如果个数超过了要求的 k，就要向左边区间查找
        if count >= self.k:
            return self.binary_search(start, mid)
        # 如果个数不够 k，就要向右边区间查找
        else:
            return self.binary_search(mid + 1, end)

    def findKthSmallest(self, coins, k):
        """
        100267.单面值组合的第 K 小金额
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        self.coins, self.k = coins, k
        self.m = min(self.coins) * k
        for i in range(len(self.coins)):
            self.lcms.append([])
        # 回溯求所有组合的 lcm
        self.backtracking(0)
        return self.binary_search(0, self.m)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthSmallest(coins=[3, 2, 6, 4, 5], k=9))
