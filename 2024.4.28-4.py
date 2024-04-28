class Solution(object):
    def count_sub(self, nums, unique):
        """
        计算不同元素个数小于等于 unique 的子数组个数。
        :type nums: List[int]
        :type unique: int
        :rtype: int
        """
        # 子数组个数
        count = 0
        # 滑动窗口的左右边界
        left, right = 0, 0
        # 当前滑动窗口内不同的元素
        unique_num = set()
        # 当前滑动窗口内不同元素的对应个数
        num_dict = {}
        while left <= right < len(nums):
            # 先把 nums[right] 加入到统计信息中
            if nums[right] not in unique_num:
                # 如果是从未出现过的元素
                num_dict.setdefault(nums[right], 0)
                unique_num.add(nums[right])
            num_dict[nums[right]] += 1
            # 判断当前滑动窗口内不同的元素个数是否小于等于 unique
            while left <= right and len(unique_num) > unique:
                num_dict[nums[left]] -= 1
                if num_dict[nums[left]] == 0:
                    unique_num.remove(nums[left])
                left += 1
            # 以 nums[right] 为尾，在滑动窗口内的子数组个数和滑动窗口的长度相同
            count += (right - left + 1)
            right += 1
        return count

    def binary_search(self, nums, start, end, target):
        """
        二分搜索唯一性数组的中位数
        :type nums: List[int]
        :type start: int
        :type end: int
        :type target: int
        :rtype: int
        """
        # 终止条件
        if start >= end:
            return start
        mid = int((start + end) / 2)
        # 当不同元素的个数为 mid 时，<= mid 的子数组个数有多少个
        count = self.count_sub(nums, mid)
        if count == target:
            return mid
        elif count > target:
            return self.binary_search(nums, start, mid, target)
        else:
            return self.binary_search(nums, mid + 1, end, target)

    def medianOfUniquenessArray(self, nums):
        """
        100257.找出唯一性数组的中位数
        二分搜索 + 滑动窗口
        :type nums: List[int]
        :rtype: int
        """
        # 整个数组中不同元素的个数
        unique_num = set()
        for num in nums:
            if num not in unique_num:
                unique_num.add(num)
        # 所有子数组个数
        sub_count = int((1 + len(nums)) * len(nums) / 2)
        return self.binary_search(nums, 1, len(unique_num), int((sub_count + 1) / 2))


if __name__ == "__main__":
    sol = Solution()
    print(sol.medianOfUniquenessArray(nums=[91, 64, 76, 18, 61, 55, 46, 93, 65, 99]))
    # print(sol.count_sub(nums=[3, 4, 3, 4, 5], unique=1))
