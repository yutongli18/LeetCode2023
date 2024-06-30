class Solution(object):
    def maximumLength(self, nums):
        """
        100357.找出有效子序列的最大长度 I
        :type nums: List[int]
        :rtype: int
        """
        # max_length = 0
        # # dp = [相邻和为偶数的长度，相邻和为奇数的长度]
        # # nums[i] 为奇数的数对
        # odd_dp = [0, 0]
        # # nums[i] 为偶数的数对
        # even_dp = [0, 0]
        # for i in range(len(nums)):
        #     dp = [0, 0]
        #     if nums[i] % 2 == 0:
        #         # nums[i] 为偶数
        #         dp[0] = even_dp[0] + 1
        #         dp[1] = odd_dp[1] + 1
        #         even_dp = dp[:]
        #     else:
        #         # nums[i] 为奇数
        #         dp[0] = odd_dp[0] + 1
        #         dp[1] = even_dp[1] + 1
        #         odd_dp = dp[:]
        #     max_length = max(max_length, dp[0], dp[1])
        # return max_length

        # dp[i][j] 表示 sub[x - 2] mod 2 = i, sub[x - 1] mod 2 = j
        dp = [[0 for _ in range(2)] for _ in range(2)]
        for num in nums:
            j = num % 2
            dp[0][j] = dp[j][0] + 1
            dp[1][j] = dp[j][1] + 1
        return max(max(x) for x in dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumLength(nums=[1, 3]))
