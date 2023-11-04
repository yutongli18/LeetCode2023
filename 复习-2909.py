class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum_sum = -1
        # 记录前缀最小值
        prefix_min = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix_min[i] = nums[i]
            else:
                prefix_min[i] = min(prefix_min[i - 1], nums[i])
        # 记录后缀最小值
        postfix_min = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix_min[i] = nums[i]
            else:
                postfix_min[i] = min(postfix_min[i + 1], nums[i])
        # 遍历 mid
        for mid_index in range(1, len(nums) - 1):
            left = prefix_min[mid_index - 1]
            right = postfix_min[mid_index + 1]
            if nums[mid_index] > left and nums[mid_index] > right:
                minimum_sum = min(minimum_sum, left + nums[mid_index] + right) if minimum_sum != -1 \
                    else (left + nums[mid_index] + right)
        return minimum_sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSum(nums=[6, 5, 4, 3, 4, 5]))
