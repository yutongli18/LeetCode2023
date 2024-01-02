class Solution(object):
    def check(self, num):
        """
        检测某个数字是否是回文数。
        :param num: int
        :return: bool
        """
        num_list = []
        rest = num
        while rest > 0:
            num_list.append(rest % 10)
            rest = int(rest / 10)
        left, right = 0, len(num_list) - 1
        while left < right:
            if num_list[left] != num_list[right]:
                return False
            left += 1
            right -= 1
        return True

    def compute_count(self, nums, target):
        """
        计算总代价。
        :param nums: List[int]
        :param target: int
        :return: int
        """
        total_count = 0
        for num in nums:
            total_count += abs(num - target)
        return total_count

    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        mid1 = (n - 1) // 2
        mid2 = n // 2
        target1, target2 = nums[mid1], nums[mid2]
        while not self.check(num=target1):
            target1 += 1
        while not self.check(num=target2):
            target2 -= 1
        return min(self.compute_count(nums=nums, target=target1), self.compute_count(nums=nums, target=target2))


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumCost(nums=[1, 2, 3, 4, 5]))
