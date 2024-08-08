class Solution(object):
    def binarySearchMedian(self, nums1, nums2, target):
        """
        在nums1和nums2中二分搜索第target位数字
        :param nums1: List[int]
        :param nums2: List[int]
        :param target: int
        :return: int
        """
        if len(nums1) == 0:
            return nums2[target - 1]
        if len(nums2) == 0:
            return nums1[target - 1]
        if target == 1:
            return min(nums1[0], nums2[0])
        index1 = min(target // 2 - 1, len(nums1) - 1)
        index2 = min(target // 2 - 1, len(nums2) - 1)
        if nums1[index1] >= nums2[index2]:
            return self.binarySearchMedian(nums1, nums2[index2 + 1:], target - index2 - 1)
        else:
            return self.binarySearchMedian(nums1[index1 + 1:], nums2, target - index1 - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        4.寻找两个正序数组的中位数
        问题在于，是找nums1和nums2中第k位的数字，它必须在nums1和nums2中存在，比之前做过的二分搜索要困难
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 0:
            index = (m + n) // 2
            return (self.binarySearchMedian(nums1, nums2, index) + self.binarySearchMedian(nums1, nums2, index + 1)) / 2.0
        else:
            index = (m + n) // 2 + 1
            return self.binarySearchMedian(nums1, nums2, index)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
