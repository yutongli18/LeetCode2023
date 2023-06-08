"""
31.下一个排列
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numsLength = len(nums)
        index = -1
        for i in range(numsLength - 2, -1, -1):
            if nums[i] < nums[i + 1]:  # 从右边开始找第一个比它的下一个数字要小的数字
                index = i
                # print(index)
                for j in range(numsLength - 1, index, -1):
                    if nums[i] < nums[j]:  # 换一个比原来位置更大的数字
                        nums[i], nums[j] = nums[j], nums[i]
                        break
            if index != -1:  # 因为只要找下一个排列，只要找到就可以提前离开了，否则可能会换多次，导致最终结果错误
                break
        left, right = index + 1, numsLength - 1  # 剩下的元素直接按升序排列即可，能让变化尽可能小
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            # print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    sol.nextPermutation(nums=nums)
    print(nums)
