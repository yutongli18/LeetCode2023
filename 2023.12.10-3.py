class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums)
        # print(max_num)
        prefix = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == max_num:
                prefix[i] = prefix[i - 1] + 1 if i > 0 else 1
            else:
                prefix[i] = prefix[i - 1] if i > 0 else 0
        # print(prefix)
        count = 0
        if prefix[-1] < k:
            return count
        left, right = 0, 0
        while left < len(nums):
            lower = prefix[left - 1] if left > 0 else 0
            while right < len(nums) and prefix[right] < lower + k:
                right += 1
            if right >= len(nums):
                break
            count += (len(nums) - right)
            left += 1
            if left > right:
                right += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(
        sol.countSubarrays(nums=[21, 11, 13, 15, 16, 21, 8, 9, 6, 21], k=2))
