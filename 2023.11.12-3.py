"""
100117. 最大化数组末位元素的最少操作次数
贪心。
"""


class Solution(object):
    def count_swaps(self, nums1, nums2, is_swap):
        count = 0
        if is_swap:
            last1, last2 = nums2[-1], nums1[-1]
            count += 1
        else:
            last1, last2 = nums1[-1], nums2[-1]
        for index in range(len(nums1) - 1):
            if nums1[index] > last1 or nums2[index] > last2:
                if nums1[index] > last2 or nums2[index] > last1:
                    return -1
                count += 1
        return count

    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 最后一个元素只有交换和不交换两种可能
        # 如果最后一个元素交换
        ans1 = self.count_swaps(nums1=nums1[:], nums2=nums2[:], is_swap=True)
        ans2 = self.count_swaps(nums1=nums1[:], nums2=nums2[:], is_swap=False)
        if ans1 < 0:
            if ans2 < 0:
                return -1
            else:
                return ans2
        else:
            if ans2 < 0:
                return ans1
            else:
                return min(ans1, ans2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(nums1=[1, 2, 7], nums2=[4, 5, 3]))
