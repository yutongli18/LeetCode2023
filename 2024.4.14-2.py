class Solution(object):
    def isPrime(self, num):
        if num == 1:
            return False
        if num in [2, 3, 5, 7]:
            return True
        for i in range(2, 10):
            if num % i == 0:
                return False
        return True

    def maximumPrimeDifference(self, nums):
        """
        100265.素数的最大距离
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and not self.isPrime(nums[left]):
            left += 1
        while left < right and not self.isPrime(nums[right]):
            right -= 1
        return right - left


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumPrimeDifference(nums=[1, 7]))
