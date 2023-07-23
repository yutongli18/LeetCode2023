"""
344.反转字符串
双指针
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_length = len(s)
        left, right = 0, s_length - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


if __name__ == '__main__':
    sol = Solution()
    sol.reverseString(s=["h", "e", "l", "l", "o"])
