class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        673. 最长递增子序列的个数
        dp[i]：以 nums[i] 为尾的 [最长递增子序列长度, 最长递增子序列个数]
        必须记录长度，否则无法知道什么时候出现最长的递增子序列。
        同时必须记录个数，最长的递增子序列可能有不同的来源，把这些来源求和即可。
        :type nums: List[int]
        :rtype: int
        """
        max_length, max_count = 1, 1
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for k in range(i):
                if nums[i] > nums[k]:
                    # 如果找到了长度更长的递增子序列，就更新最长递增子序列长度和个数
                    # 个数就是以 nums[k] 为尾的最长递增子序列个数
                    if dp[k][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[k][0] + 1
                        dp[i][1] = dp[k][1]
                    # 如果找到了长度相同的递增子序列，就更新最长递增子序列的个数
                    # 新的个数要加上以 nums[k] 为尾的最长递增子序列个数
                    elif dp[k][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[k][1]
            if dp[i][0] > max_length:
                max_length = dp[i][0]
                max_count = dp[i][1]
            elif dp[i][0] == max_length:
                max_count += dp[i][1]
        return max_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumberOfLIS(nums=[1, 2, 4, 3, 5, 4, 7, 2]))
