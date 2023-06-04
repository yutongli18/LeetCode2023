"""
2465.不同的平均值数目
"""


class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        avg = set()
        while nums:
            # print(nums)
            avg.add((nums.pop(0) + nums.pop(-1)) / 2)
            print(avg)
        return len(avg)


if __name__ == '__main__':
    sol = Solution()
    print(sol.distinctAverages(nums=[9, 5, 7, 8, 7, 9, 8, 2, 0, 7]))
