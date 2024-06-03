class Solution(object):
    def minimumDifference(self, nums, k):
        """
        100315.找到按位与最接近 K 的子数组
        找最接近的两个数字？不可行，这样不一定能得到最小的。
        找 nums 中所有的按位与运算结果（优化）。
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_diff = abs(nums[0] - k)
        # 原地求按位与结果
        # 在每层循环中，nums[j] 保存从 nums[j] 到 nums[i] 这段区间的与运算结果
        for i in range(1, len(nums)):
            min_diff = min(min_diff, abs(nums[i] - k))
            # for j in range(i - 1, -1, -1):
            #     if nums[j] & nums[i] == nums[j]:
            #         # 那么，从 nums[j] 开始再往左侧的所有元素和 nums[i] 的与运算结果也一定等于其本身，没必要继续计算了
            #         break
            #     else:
            #         nums[j] = nums[j] & nums[i]
            #     min_diff = min(min_diff, abs(nums[j] - k))
            j = i - 1
            while j >= 0 and nums[j] & nums[i] != nums[j]:
                nums[j] = nums[j] & nums[i]
                min_diff = min(min_diff, abs(nums[j] - k))
                j -= 1
        return min_diff


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDifference(nums=[1], k=10))
