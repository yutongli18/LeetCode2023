class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        100308.特殊数组 II
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # 求 nums 中以 nums[i] 为终点的特殊数组的起点是哪个索引
        special_start = [i for i in range(len(nums))]
        is_odd = True if nums[0] % 2 != 0 else False
        start = 0
        for i in range(1, len(nums)):
            curr = (nums[i] % 2 != 0)
            # 如果不满足特殊数组的条件，那么以 nums[i] 为终点的特殊数组的起点只能是 nums[i] 本身
            if curr ^ is_odd == 0:
                special_start[i] = i
                start = i
            else:
                special_start[i] = start
            is_odd = curr
        # 结果
        answer = []
        for [start, end] in queries:
            if start == end:
                answer.append(True)
                continue
            if start >= special_start[end]:
                answer.append(True)
            else:
                answer.append(False)
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
