class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        100287.找出与数组相加的整数 II
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        # nums2 中相邻两数之间的差值
        nums2_diff = [nums2[i + 1] - nums2[i] for i in range(len(nums2) - 1)]
        right = len(nums1) - 1
        while right >= 0:
            # 目前，选择 nums1[right] 作为保留的元素，要找到能保留的其它元素
            mid = right
            left = right - 1
            total_count = len(nums2) - 1
            while left >= 0 and mid >= 0 and total_count > 0:
                while left >= 0 and nums1[mid] - nums1[left] != nums2_diff[total_count - 1]:
                    left -= 1
                if left < 0:
                    break
                mid = left
                left = mid - 1
                total_count -= 1
            if total_count <= 0:
                # 说明找到了一组最大的和 nums2 对应的 nums1
                return nums2[-1] - nums1[right]
            right -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumAddedInteger(nums1=[3, 5, 5, 3], nums2=[7, 7]))
