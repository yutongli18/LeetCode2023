class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        curr_sum1, curr_sum2 = 0, 0
        zero_count1, zero_count2 = 0, 0
        for num in nums1:
            curr_sum1 += num
            if num == 0:
                zero_count1 += 1
        for num in nums2:
            curr_sum2 += num
            if num == 0:
                zero_count2 += 1

        # 如果两个数组中都没有可以替换的 0，那么直接结束
        if zero_count1 == 0 and zero_count2 == 0:
            if curr_sum1 == curr_sum2:
                return curr_sum1
            else:
                return -1

        target = 0
        # 如果有一个数组中没有 0，那么另一个数组只能往这个数组的方向凑值
        if zero_count1 == 0:
            target = curr_sum1
            if target - curr_sum2 >= zero_count2:
                return target
            else:
                return -1
        elif zero_count2 == 0:
            target = curr_sum2
            if target - curr_sum1 >= zero_count1:
                return target
            else:
                return -1
        # 如果两个数组中都有 0，那么小值往大值凑
        else:
            pad_num = 1
            while True:
                # 交换一下顺序，让 curr_sum1 是较小的那一个
                if curr_sum1 + pad_num * zero_count1 > curr_sum2 + pad_num * zero_count2:
                    curr_sum1, curr_sum2 = curr_sum2, curr_sum1
                    zero_count1, zero_count2 = zero_count2, zero_count1
                target = curr_sum2 + zero_count2 * pad_num
                if target - curr_sum1 >= zero_count1:
                    return target
                pad_num += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4]))
