"""
189.轮转数组
"""


class Solution(object):
    def list_reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # pos_nums = nums[:]
        # for i in range(len(nums)):
        #     j = int((i - k + len(nums)) % len(nums))
        #     nums[i] = pos_nums[j]
        # 右旋数组，相当于先反转整个数组，然后对前 k 区间和后 len(nums) - k 区间分别反转
        k = k % len(nums)
        nums.reverse()
        self.list_reverse(nums, 0, k - 1)
        self.list_reverse(nums, k, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    print(nums)
