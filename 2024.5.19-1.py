class Solution(object):
    def isArraySpecial(self, nums):
        """
        100310.特殊数组 I
        :type nums: List[int]
        :rtype: bool
        """
        # 上一个检查的数字的奇偶性 True-奇数 False-偶数
        is_odd = True if nums[0] % 2 != 0 else False
        for i in range(1, len(nums)):
            if (nums[i] % 2 != 0) ^ is_odd == 0:
                return False
            is_odd = (nums[i] % 2 != 0)
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isArraySpecial(nums=[2, 1, 4]))
