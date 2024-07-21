class Solution(object):
    def minimumOperations(self, nums, target):
        """
        100329.使数组等于目标数组所需的最少操作次数
        子数组的变化可以转换成差分数组的变化
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        total = 0
        # 把i=0的情况单独拿出来考虑
        k = target[0] - nums[0]
        total += abs(k)
        s = k
        # 一边求差分数组一边计算
        i = 1
        while i < len(nums):
            k = (target[i] - target[i - 1]) - (nums[i] - nums[i - 1])
            if k >= 0:
                if s >= 0:
                    total += k
                else:
                    total += max(k - abs(s), 0)
            else:
                if s <= 0:
                    total += abs(k)
                else:
                    total += max(abs(k) - s, 0)
            s += k
            i += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumOperations([9, 2, 6, 10, 4, 8, 3, 4, 2, 3], [9, 5, 5, 1, 7, 9, 8, 7, 6, 5]))
