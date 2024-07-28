import math


class Solution(object):
    def __init__(self):
        self.next_zero = []

    def numberOfSubstrings(self, s):
        """
        Q3.统计1显著字符串的数量
        :type s: str
        :rtype: int
        """
        total = 0
        # 可以遍历的0的数量的上限
        zero_limit = math.isqrt(len(s))
        # 记录s[i]之后下一个0的位置
        self.next_zero = [0 for _ in range(len(s))]
        pos_zero = len(s)
        for i in range(len(s) - 1, -1, -1):
            self.next_zero[i] = pos_zero
            if s[i] == "0":
                pos_zero = i
        # 遍历所有可能的左边界
        for left in range(len(s)):
            cnt = [0, 0]  # 统计子串内0/1的数量
            # 右边界为下一个0的位置
            right = left
            if s[left] == "0":
                cnt[0] += 1
            while right < len(s):
                if cnt[0] > zero_limit:
                    break
                # 右边界往右下一个0的位置
                r_right = self.next_zero[right]
                cnt[1] = right - left + 1 - cnt[0]
                total += max(0, r_right - right - max(cnt[0] ** 2 - cnt[1], 0))
                right = r_right
                cnt[0] += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubstrings("00011"))
