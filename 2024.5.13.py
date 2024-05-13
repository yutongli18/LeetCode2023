class Solution(object):
    def longestConsecutive(self, nums):
        """
        128.最长连续序列
        哈希表
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        # 以 key 为端点的区间长度
        point_length = {}
        # 不重复的元素集合
        num_set = set()
        for num in nums:
            # 已经在区间内部的点不重复计算
            if num in num_set:
                continue
            # 取出左右相邻区间的长度
            left_length = point_length.get(num - 1, 0)
            right_length = point_length.get(num + 1, 0)
            # 加上 num 之后连接而成的新长度
            curr_length = left_length + right_length + 1
            # 考虑到 left_length 或 right_length 可能为 0
            point_length.setdefault(num, curr_length)
            # 更新区间端点的长度
            if left_length > 0:
                point_length[num - left_length] = curr_length
            if right_length > 0:
                point_length[num + right_length] = curr_length
            # 更新集合
            num_set.add(num)
            # 更新最大值
            max_length = max(max_length, curr_length)
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
