"""
376. 摆动序列
贪心算法，O(n)时间复杂度。
统计谷底和山峰出现的次数。
"""


class Solution(object):
    def __init__(self):
        self.pre_diff = 0
        self.curr_diff = 0
        self.result = 1

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums) - 1):
            self.curr_diff = nums[index + 1] - nums[index]
            # 出现谷底或山峰
            # 注意：平顶山峰或平底山谷也要算 1 个
            if (self.pre_diff <= 0 and self.curr_diff > 0) or (self.pre_diff >= 0 and self.curr_diff < 0):
                self.result += 1
                # self.pre_diff 和 self.curr_diff 的数值不重要，重要的是正负
                # 只有出现波动的时候才更新 self.pre_diff，这样能避开连续上坡或连续下坡的情况
                self.pre_diff = self.curr_diff
        return self.result


if __name__ == '__main__':
    sol = Solution()
    print(sol.wiggleMaxLength(nums=[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
