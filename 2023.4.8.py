"""
18.四数之和
排序+双指针。关键在于如何剪枝。
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numsLength = len(nums)
        sortedNums = sorted(nums)
        resultList = []
        for i in range(numsLength-3):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:  # 剪枝：否则会有重复
                continue
            for j in range(i+1, numsLength-2):
                if j > i+1 and sortedNums[j] == sortedNums[j-1]:  # 剪枝
                    continue
                for left in range(j+1, numsLength-1):
                    if left > j+1 and sortedNums[left] == sortedNums[left-1]:  # 剪枝
                        continue
                    right = numsLength - 1
                    while left < right \
                            and sortedNums[i] + sortedNums[j] + sortedNums[left] + sortedNums[right] > target:
                        right -= 1
                    if left < right \
                            and sortedNums[i] + sortedNums[j] + sortedNums[left] + sortedNums[right] == target:
                        resultList.append([sortedNums[i], sortedNums[j], sortedNums[left], sortedNums[right]])
        return resultList


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum(nums=[2, 2, 2, 2, 2], target=8))
