class Solution(object):
    def maximumLength(self, nums, k):
        """
        100358.找出有效子序列的最大长度 II
        直接动态规划超时
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # max_length = 0
        # dp = [[1 for _ in range(k)] for _ in range(len(nums))]
        # for i in range(1, len(nums)):
        #     for r in range(k):
        #         j = i - 1
        #         while j >= 0 and (nums[j] + nums[i]) % k != r:
        #             j -= 1
        #         if j >= 0:
        #             dp[i][r] = dp[j][r] + 1
        #     max_length = max(max_length, max(dp[i]))
        # return max_length

        # dp[i][j] 表示最后一位 mod k 为 j，倒数第二位 mod k 为 i 的子序列长度
        dp = [[0 for _ in range(k)] for _ in range(k)]
        for num in nums:
            j = num % k
            for r in range(k):
                dp[r][j] = dp[j][r] + 1
        return max(max(x) for x in dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumLength(nums=[1, 9, 3, 10, 10], k=4))
