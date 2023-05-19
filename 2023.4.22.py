"""
1027.最长等差数列
动态规划。
动态规划可能有不止一个参数。
"""


class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue, minValue = max(nums), min(nums)
        maxDiff = maxValue - minValue
        maxLength = 1

        for diff in range(-maxDiff, maxDiff+1):  # 等差数列可能的公差
            length = {}
            for num in nums:
                pre = num - diff
                if pre in length:
                    length[num] = max(length[pre] + 1, length.get(num, 0))
                    maxLength = max(maxLength, length[num])
                length[num] = max(length.get(num, 0), 1)  # 考虑单独成序列的情况
        return maxLength


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestArithSeqLength(nums=[9, 4, 7, 2, 10]))
