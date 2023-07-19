"""
454.四数相加II
哈希表。
注意：
① 遍历三个数组，再到第四个数组里去找的时间复杂度为 O(n3)，会超时，那先遍历两个数组，再到最后两个数组中去找，时间复杂度就会降低到 O(n2)
"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        target = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                total = nums1[i] + nums2[j]
                target.setdefault(0 - total, 0)
                target[0 - total] += 1
        # print(target)
        count = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                total = nums3[i] + nums4[j]
                if target.get(total) is not None:
                    count += target[total]
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]))
