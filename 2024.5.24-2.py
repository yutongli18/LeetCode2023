class Solution(object):
    def productExceptSelf(self, nums):
        """
        238.除自身以外数组的乘积
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0 for _ in range(len(nums))]
        # 先按照前缀乘积算一遍
        pre_prod = 1
        for i in range(len(nums)):
            answer[i] = pre_prod
            pre_prod *= nums[i]
        # 再按照后缀乘积算一遍
        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post_prod
            post_prod *= nums[i]
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
