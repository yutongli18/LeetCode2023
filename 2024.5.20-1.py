class Solution(object):
    def subarraySum(self, nums, k):
        """
        560.和为 K 的子数组
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        # 前缀和
        pre_sum = 0
        # 前缀和字典
        sum_dict = {0: 1}
        for num in nums:
            pre_sum += num
            sum_dict.setdefault(pre_sum - k, 0)
            count += sum_dict[pre_sum - k]
            sum_dict.setdefault(pre_sum, 0)
            sum_dict[pre_sum] += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum(nums=[1, -1, 0], k=0))
