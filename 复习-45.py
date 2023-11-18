class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        if len(nums) == 1:
            return steps
        curr_cover, next_cover = 0, 0
        index = 0
        while index <= curr_cover:
            next_cover = max(next_cover, index + nums[index])
            if index == curr_cover:
                steps += 1
                curr_cover = next_cover
                if curr_cover >= len(nums) - 1:
                    return steps
            index += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.jump(nums=[0]))
