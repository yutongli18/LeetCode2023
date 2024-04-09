class Solution(object):
    def backspaceCompare(self, s, t):
        """
        844. 比较退格的字符串
        双指针解法（空间复杂度 O(1)）
        :type s: str
        :type t: str
        :rtype: bool
        """
        left, right = len(s) - 1, len(t) - 1
        while True:
            skip_s, skip_t = 0, 0
            while left >= 0:
                if s[left] == '#':
                    skip_s += 1
                    left -= 1
                else:
                    if skip_s > 0:
                        left -= 1
                        skip_s -= 1
                    else:
                        break
            while right >= 0:
                if t[right] == '#':
                    skip_t += 1
                    right -= 1
                else:
                    if skip_t > 0:
                        right -= 1
                        skip_t -= 1
                    else:
                        break
            if left < 0 or right < 0:
                break
            if s[left] != t[right]:
                return False
            left -= 1
            right -= 1
        if left >= 0 or right >= 0:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare(s='ab##', t='a#b#'))
