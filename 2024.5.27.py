class Solution(object):
    def firstMissingPositive(self, nums):
        """
        41.缺失的第一个正数
        找最小的连续区间范围？不可用，参考用例：[1, 2, 6, 3, 5, 4]，最后的 4 把前后两段区间连接起来了。
        原地哈希。
        :type nums: List[int]
        :rtype: int
        """
        upper_bound = len(nums)
        # 原地哈希
        i = 0
        while i < upper_bound:
            # nums[nums[i] - 1] != nums[i] 是为了防止数组中的值有重复的情况
            if 0 < nums[i] <= upper_bound and nums[nums[i] - 1] != nums[i]:
                # 把值放到对应的位置上
                num = nums[i]
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1
        # 重新遍历数组，看哪个位置上的值不对
        i = 0
        while i < upper_bound:
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return upper_bound + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive(nums=[7, 8, 9, 11, 12]))
