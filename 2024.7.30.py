class Solution(object):
    def binary_search_rotate(self, nums, start, end, target):
        # print(start, end)
        if end < start:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 找更大的值
            if nums[mid] > nums[start]:
                # 说明nums[start:mid+1]单调递增
                return self.binary_search_rotate(nums, mid + 1, end, target)
            else:
                # 说明nums[start:mid+1]包含旋转过的部分
                if nums[end] >= target:
                    # 说明target应该在mid的右边
                    return self.binary_search_rotate(nums, mid + 1, end, target)
                else:
                    # 说明target应该在mid的左边
                    return self.binary_search_rotate(nums, start, mid - 1, target)
        else:
            # 找更小的值
            if nums[mid] >= nums[start]:
                # 说明nums[start:mid+1]单调递增
                if nums[start] <= target:
                    # 说明target在mid的左边
                    return self.binary_search_rotate(nums, start, mid - 1, target)
                else:
                    # 说明target在mid的右边
                    return self.binary_search_rotate(nums, mid + 1, end, target)
            else:
                # 说明nums[start:mid+1]包含旋转后的部分
                return self.binary_search_rotate(nums, start, mid - 1, target)

    def search(self, nums, target):
        """
        33.搜索旋转排序数组
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search_rotate(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([3, 1], 1))
