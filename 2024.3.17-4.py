"""
100227.拾起 K 个 1 需要的最少行动次数
"""


class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        index = -1  # index 位置
        default_index = 1  # 默认 index 位置
        for i in range(1, len(nums) - 1):
            if nums[i] == 1:
                if nums[i - 1] == 1 and nums[i + 1] == 1:  # 最佳位置，如果能找到，就不再往下找了
                    index = i
                    return
                elif nums[i - 1] == 1 or nums[i + 1] == 1:  # 次优位置，如果找到，先赋值看看能不能找到最优位置
                    index = i
                else:
                    default_index = i
        if index <= 0:
            index = default_index
        # 开始计数
        count = 0
        while k > 0:
            if nums[index] == 1:  # 如果已经是 1，直接拾起，不计入执行步骤
                k -= 1
                nums[index] = 0
                continue
            # 如果不是 1，看能否从左右换到 1
            if nums[index - 1] == 1:
                nums[index - 1], nums[index] = nums[index], nums[index - 1]
                count += 1
                continue
            if nums[index + 1] == 1:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                count += 1
                continue
            # 如果左右都没法换到 1，那就只能把左右赋值成 1
            if maxChanges >= 2:
                nums[index - 1] = 1
                nums[index + 1] = 1
                count += 2
            elif maxChanges == 1:
                nums[index - 1] = 1
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumMoves(nums=[0, 0, 0, 0], k=2, maxChanges=3))
