class Solution(object):
    def get_count(self, nums1, last1, nums2, last2, count):
        for index in range(len(nums1) - 1):
            if nums1[index] > last1 or nums2[index] > last2:
                if nums1[index] <= last2 and nums2[index] <= last1:
                    count += 1
                else:
                    count = -1
                    break
        return count

    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        no_change_count = self.get_count(nums1=nums1, last1=nums1[-1], nums2=nums2, last2=nums2[-1], count=0)
        change_count = self.get_count(nums1=nums1, last1=nums2[-1], nums2=nums2, last2=nums1[-1], count=1)
        count = min(no_change_count, change_count)
        return count if count <= len(nums1) else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(nums1=[2, 3, 4, 5, 9], nums2=[8, 8, 4, 4, 4]))
