class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        """
        100288.使数组中所有元素相等的最小开销。
        max(nums) 不一定是最后的结果。
        :type nums: List[int]
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        total_cost = 0
        # 如果 nums 中只有一个元素，则无需操作
        if len(nums) == 1:
            return total_cost
        # 如果 nums 中只有两个元素，此时只能选择操作一，目标是 nums 中较大的那一个
        if len(nums) == 2:
            return (cost1 * (max(nums) - min(nums))) % (10 ** 9 + 7)
        # 如果执行两步操作一比执行一步操作二更有利，那么只选择操作一即可
        if 2 * cost1 <= cost2:
            target = max(nums)
            for num in nums:
                total_cost += cost1 * (target - num)
            return total_cost % (10 ** 9 + 7)
        # 剩余的情况要尽可能执行操作二，实在不行的时候再执行操作一
        min_num = min(nums)
        max_num = max(nums)
        min_cost = 10 ** 18
        # 需要执行的操作总数
        total_ops = max_num * len(nums) - sum(nums)
        # 需要执行的最多操作数
        max_ops = max_num - min_num
        for target in range(max_num, max_num * 2 + 1):
            total_cost = 0
            # 说明可以用 max_ops 对应的这个元素和其它所有元素都执行完操作二，最后剩下的是这个元素
            if max_ops > total_ops - max_ops:
                total_cost += cost2 * (total_ops - max_ops) + cost1 * (max_ops - (total_ops - max_ops))
            # 总共能执行 total_ops // 2 次操作二，如果 total_ops 是奇数，最后会剩下一次，需要执行操作一
            else:
                if total_ops % 2 == 0:
                    total_cost += cost2 * (total_ops // 2)
                else:
                    total_cost += (cost2 * (total_ops // 2) + cost1)
            min_cost = min(min_cost, total_cost)
            # 目标数每增加1，总操作数增加 len(nums) 次，最大操作数增加 1 次
            total_ops += len(nums)
            max_ops += 1
        return min_cost % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostToEqualizeArray(nums=[1, 1000000, 999999], cost1=1000000, cost2=1))
