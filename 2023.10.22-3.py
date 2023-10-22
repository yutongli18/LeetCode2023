"""
100097. 合法分组的最少组数
分情况模拟。
"""


from collections import Counter


class Solution(object):
    def checkK(self, total_counts, k):
        # 第一种情况：尝试把物品分为 k + 1 数量的小组
        num_groups_1 = int(total_counts / (k + 1))
        rest = total_counts % (k + 1)
        if num_groups_1 + rest >= k:
            num_groups_1 += 1
        else:
            num_groups_1 = -1
        # 第二种情况：尝试把物品分为 k 数量的小组
        num_groups_2 = int(total_counts / k)
        rest = total_counts % k
        if rest > num_groups_2:
            num_groups_2 = -1
        # 返回当前数字的最小分组
        if num_groups_1 > 0:
            if num_groups_2 > 0:
                return min(num_groups_1, num_groups_2)
            else:
                return num_groups_1
        else:
            if num_groups_2 > 0:
                return num_groups_2
            else:
                return -1

    def minGroupsForValidAssignment(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        min_counts = min(nums_counter.values())
        min_groups = len(nums)
        for k in range(1, min_counts + 1):
            # 每组物品必须能够分为 k 和 k + 1 数量的小组
            # 否则当前的 k 不可用
            is_valid = True
            num_groups = 0
            for num in nums_counter.keys():
                groups = self.checkK(total_counts=nums_counter[num], k=k)
                if groups > 0:
                    num_groups += groups
                else:
                    is_valid = False
                    break
            if not is_valid:
                continue
            else:
                min_groups = min(min_groups, num_groups)
        return min_groups
