"""
100142. 交换得到字典序最小的数组
分组排序
"""


class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        """for index in range(len(nums)):
            if nums[index] <= 1:
                continue
            upper, lower = nums[index] - 1, nums[index] - limit
            smaller_index = index
            smaller = nums[index]
            for j in range(index + 1, len(nums)):
                if lower <= nums[j] <= upper and nums[j] < smaller:
                    smaller_index = j
                    smaller = nums[j]
            if smaller_index > index:
                nums[index], nums[smaller_index] = nums[smaller_index], nums[index]
        return nums"""
        num_list = list(enumerate(nums))
        num_list.sort(key=lambda item: item[1])
        print(num_list)
        n = len(nums)
        a = [num_list[0][0]]
        b = [num_list[0][1]]
        for i in range(1, n):
            if num_list[i][1] - num_list[i-1][1] <= limit:
                a.append(num_list[i][0])
                b.append(num_list[i][1])
            else:
                a.sort()
                m = len(a)
                for j in range(m):
                    nums[a[j]] = b[j]
                a = [num_list[i][0]]
                b = [num_list[i][1]]
        a.sort()
        m = len(a)
        for j in range(m):
            nums[a[j]] = b[j]
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicographicallySmallestArray(nums=[4, 52, 38, 59, 71, 27, 31, 83, 88, 10], limit=14))
