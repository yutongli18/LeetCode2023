class Solution(object):
    def minimumChairs(self, s):
        """
        100307.候诊室中的最少椅子数
        统计整个流程中，某个时刻的最多病人数
        :type s: str
        :rtype: int
        """
        max_chairs = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'E':
                count += 1
            else:
                count -= 1
            max_chairs = max(max_chairs, count)
        return max_chairs


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumChairs(s="ELEELEELLL"))
