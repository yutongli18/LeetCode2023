class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        100323.优质数对的总数 I
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
