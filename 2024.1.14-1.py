from collections import Counter


class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        nums_dict = [(num, count) for num, count in nums_counter.items()]
        nums_dict.sort(key=lambda item: item[1], reverse=True)
        result = 0
        prev_count = nums_dict[0][1]
        for item in nums_dict:
            if item[1] == prev_count:
                result += item[1]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxFrequencyElements(nums=[1, 2, 3, 4, 5]))
