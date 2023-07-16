"""
349. 两个数组的交集
set 集合 + 双指针/直接遍历
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums_set1 = sorted(set(nums1))
        nums_set2 = sorted(set(nums2))
        length1, length2 = len(nums_set1), len(nums_set2)
        left, right = 0, 0
        result = []
        while left < length1 and right < length2:
            if nums_set1[left] == nums_set2[right]:
                result.append(nums_set1[left])
                left += 1
                right += 1
            elif nums_set1[left] > nums_set2[right]:
                right += 1
            else:
                left += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
