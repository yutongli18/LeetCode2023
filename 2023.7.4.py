"""
209.长度最小的子数组
滑动窗口。
目前来看，滑动窗口可以解决数组中连续的序列问题。
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = 0, 0
        sum = 0
        result = n + 1
        while end < n:  # 为了一次遍历解决问题，循环标记滑动窗口末尾的位置
            sum += nums[end]
            while start <= end and sum >= target:  # 当前窗口内的和大于等于target，可以变化滑动窗口的起始位置了。
                result = min(result, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        if result > n:
            return 0
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
