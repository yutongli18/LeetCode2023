class Solution(object):
    def productExceptSelf(self, nums):
        """
        238.除自身以外数组的乘积
        :type nums: List[int]
        :rtype: List[int]
        """
        # 求前缀和后缀乘积
        pre_prod = [num for num in nums]
        post_prod = [num for num in nums]
        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i - 1] * pre_prod[i]
        for i in range(len(nums) - 2, -1, -1):
            post_prod[i] = post_prod[i + 1] * post_prod[i]
        # 根据前缀和后缀输出结果
        answer = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                answer[i] = post_prod[i + 1]
            elif i == len(nums) - 1:
                answer[i] = pre_prod[i - 1]
            else:
                answer[i] = pre_prod[i - 1] * post_prod[i + 1]
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
