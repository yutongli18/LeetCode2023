class Solution(object):
    def canAliceWin(self, nums):
        """
        Q1.判断是否可以赢得数字游戏
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        nums.sort()
        # 求所有个位数之和
        s_total = 0
        for num in nums:
            if 1 <= num <= 9:
                s_total += num
            else:
                break
        return total - s_total > s_total or s_total > total - s_total


if __name__ == "__main__":
    sol = Solution()
    print(sol.canAliceWin([5, 5, 5, 25]))
