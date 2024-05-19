class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        100300.所有数对中数位不同之和
        :type nums: List[int]
        :rtype: int
        """
        total_diff = 0
        # 每个数位单独计算
        for _ in range(1, 10):
            # 统计 0 ~ 9 每个数字的出现频次
            bit_counter = [0 for _ in range(10)]
            for i in range(len(nums)):
                bit_counter[nums[i] % 10] += 1
                nums[i] = nums[i] // 10
            for count in bit_counter:
                if count != 0:
                    total_diff += count * (len(nums) - count)
            if nums[0] == 0:
                break
        return total_diff // 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumDigitDifferences(nums=[824, 843, 837, 620, 836, 234, 276, 859]))
