class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        100285. 找出与数组相加的整数 I
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return min(nums2) - min(nums1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addedInteger(nums1=[10], nums2=[5]))
