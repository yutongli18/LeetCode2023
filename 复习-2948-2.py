class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        sorted_nums = [(num, index) for index, num in enumerate(nums)]
        sorted_nums.sort(key=lambda item: item[0])
        result_nums = [0 for _ in range(len(nums))]
        index_list = [sorted_nums[0][1]]
        num_list = [sorted_nums[0][0]]
        for i in range(1, len(nums)):
            if sorted_nums[i][0] - num_list[-1] <= limit:
                index_list.append(sorted_nums[i][1])
                num_list.append(sorted_nums[i][0])
            else:
                index_list.sort()
                for index, num in zip(index_list, num_list):
                    result_nums[index] = num
                index_list = [sorted_nums[i][1]]
                num_list = [sorted_nums[i][0]]
        index_list.sort()
        for index, num in zip(index_list, num_list):
            result_nums[index] = num
        return result_nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicographicallySmallestArray(nums=[1, 5, 3, 9, 8], limit=2))
