"""
18.四数之和
两层循环 + 双指针
注意：Python 的 for 循环好像和 C++ 的不太一样。首先，i 的取值直到最后都不会超过 range 给定的限制，所以不能用 i 来判断是否越界；
其次，感觉 i 的取值是不能跳变的，只能按照顺序来取值，如果本题的外层循环用 for，去重时会莫名其妙的出错。
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_length = len(nums)
        nums.sort()
        a = 0
        move_c, move_d = False, False
        result_list = []
        while a < nums_length - 3:
            pre_a = nums[a]
            b = a + 1
            while b < nums_length - 2:
                pre_b = nums[b]
                c, d = b + 1, nums_length - 1
                while c < d:
                    pre_c, pre_d = nums[c], nums[d]
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        result_list.append([nums[a], nums[b], nums[c], nums[d]])
                        move_c, move_d = True, True
                    elif total > target:
                        move_d = True
                    else:
                        move_c = True

                    if move_c:
                        move_c = False
                        while c < d and nums[c] == pre_c:
                            c += 1
                    if move_d:
                        move_d = False
                        while c < d and nums[d] == pre_d:
                            d -= 1
                while b < nums_length - 2 and nums[b] == pre_b:
                    b += 1
            while a < nums_length - 3 and nums[a] == pre_a:
                a += 1
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum(nums=[2, 2, 2, 2, 2], target=8))
