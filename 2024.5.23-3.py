class Solution(object):
    def rotate(self, nums, k):
        """
        189.轮转数组
        模拟循环
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        is_changed = [False for _ in range(len(nums))]
        temp = nums[0]
        i = 0
        curr_start = i
        while True:
            is_changed[i] = True
            j = (i + len(nums) - k) % len(nums)
            if j == curr_start:
                nums[i] = temp
                while i < len(nums) and is_changed[i]:
                    i += 1
                if i >= len(nums):
                    break
                temp = nums[i]
                curr_start = i
            else:
                nums[i] = nums[j]
                i = j


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    sol = Solution()
    sol.rotate(nums, 2)
    print(nums)
