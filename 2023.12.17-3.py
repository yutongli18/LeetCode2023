"""
100151.使数组成为等数数组的最小代价
"""


class Solution(object):
    def check_palindrome(self, num):
        # 判断一个数字是否为回文数
        num_list = []
        rest = num
        while rest > 0:
            num_list.append(rest % 10)
            rest = rest // 10
        left, right = 0, len(num_list) - 1
        while left < right:
            if num_list[left] != num_list[right]:
                return False
            left += 1
            right -= 1
        return True

    def compute_count(self, nums, p):
        # 计算代价
        count = 0
        for i in range(len(nums)):
            count += abs(p - nums[i])
        return count

    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # 如果nums中数字的数量是奇数，mid_idx1 == mid_idx2，那么lower和upper相当于是中位数左右两侧的回文数
        # 如果nums中的数字数量是偶数，mid_idx1 != mid_idx2，那么lower和upper相当于是夹在中间两个中位数中间的回文数（或者在中位数两侧）
        mid_idx1, mid_idx2 = (n - 1) // 2, n // 2
        lower, upper = nums[mid_idx1], nums[mid_idx2]
        while not self.check_palindrome(num=lower):
            lower += 1
        while not self.check_palindrome(num=upper):
            upper -= 1
        return min(self.compute_count(nums=nums, p=lower), self.compute_count(nums=nums, p=upper))


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(nums=[101, 115, 116, 120, 122]))
