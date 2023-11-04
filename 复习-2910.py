from collections import Counter


class Solution(object):
    def minGroupsForValidAssignment(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum_groups = len(nums)
        # 原始分组
        nums_counter = Counter(nums)
        k_upper = len(nums)
        for num, freq in nums_counter.items():
            k_upper = min(k_upper, freq)
        # 开始遍历 k 的值
        for k in range(1, k_upper + 1):
            # 每轮遍历 k 的最开始要把是否能分组成功的布尔变量还原
            # 否则下一个循环会受到上一个循环的影响
            is_grouped = True
            curr_groups = len(nums_counter)
            for num, freq in nums_counter.items():
                is_k_grouped, is_k1_grouped = True, True
                if freq <= k:
                    continue
                # 开始分情况讨论
                curr_groups_1, curr_groups_2 = 0, 0
                # 情况1：分成下标数量为 k + 1 的更小组
                d1 = int(freq / (k + 1))
                rest1 = freq % (k + 1)
                if rest1 == 0:
                    curr_groups_1 = curr_groups - 1 + d1
                else:
                    # 需要从前 d1 个小组中至少每个选取 1 个元素，和剩下的元素构成一个新的小组
                    if rest1 + d1 >= k:
                        curr_groups_1 = curr_groups - 1 + d1 + 1
                    else:
                        is_k1_grouped = False
                # 情况2：分成下标数量为 k 的更小组
                d2 = int(freq / k)
                rest2 = freq % k
                if rest2 == 0:
                    curr_groups_2 = curr_groups - 1 + d2
                else:
                    # 需要把剩下的元素插入到前 d2 个小组中去
                    if rest2 <= d2:
                        curr_groups_2 = curr_groups - 1 + d2
                    else:
                        is_k_grouped = False
                if is_k1_grouped:
                    if is_k_grouped:
                        curr_groups = min(curr_groups_1, curr_groups_2)
                    else:
                        curr_groups = curr_groups_1
                else:
                    if is_k_grouped:
                        curr_groups = curr_groups_2
                    else:
                        is_grouped = False
                        break
            if not is_grouped:
                continue
            else:
                minimum_groups = min(minimum_groups, curr_groups)
        return minimum_groups


if __name__ == '__main__':
    sol = Solution()
    print(sol.minGroupsForValidAssignment(nums=[1, 1, 1, 1, 1]))
