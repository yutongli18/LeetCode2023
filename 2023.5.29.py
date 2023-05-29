class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summary, count = 0, 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                count += 1
                summary += num
        return int(summary / count) if count > 0 else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.averageValue(nums=[1, 2, 4, 7, 10]))
