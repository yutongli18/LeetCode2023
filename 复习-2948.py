class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        result = [0 for _ in range(len(nums))]
        num_list = list(enumerate(nums))
        num_list.sort(key=lambda item: item[1])
        num_group = [num_list[0][1]]
        idx_group = [num_list[0][0]]
        for i in range(1, len(num_list)):
            if abs(num_list[i][1] - num_group[-1]) <= limit:
                num_group.append(num_list[i][1])
                idx_group.append(num_list[i][0])
            else:
                idx_group.sort()
                for j in range(len(num_group)):
                    result[idx_group[j]] = num_group[j]
                num_group = [num_list[i][1]]
                idx_group = [num_list[i][0]]
        idx_group.sort()
        for j in range(len(num_group)):
            result[idx_group[j]] = num_group[j]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicographicallySmallestArray(nums=[1, 60, 34, 84, 62, 56, 39, 76, 49, 38], limit=4))
