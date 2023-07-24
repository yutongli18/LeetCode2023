"""
541. 反转字符串II
注意：
① 其实不需要每轮都找到 2k 的位置，让反转的起始位置每次移动 2k 即可。
② 不管能不能到 2k，只要能到 k，就要反转前 k 个，所以其实只有 2 种情况：反转前 k 个，反转后续的全部字符串。
"""


def reverse(s, start, end):
    """
    翻转 s[start:end]
    :param s: 要反转的字符串
    :param start: 反转的开始位置（包含）
    :param end: 反转的结束位置（包含）
    :return: 反转后的字符串 s
    """
    s_list = list(s)  # 字符串本身不能做位数赋值
    left, right = start, end
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return "".join(s_list)


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_length = len(s)
        start = 0
        while start < s_length:
            end = start + k - 1
            if end < s_length:
                s = reverse(s, start, end)
                start = start + 2 * k
            else:
                s = reverse(s, start, s_length - 1)
                break
        return s


if __name__ == '__main__':
    # 测试字符串反转
    """s = "abcdefg"
    new_s = reverse(s, 4, 5)
    print(new_s)"""
    # 测试整个函数
    sol = Solution()
    print(sol.reverseStr(s="abcd", k=2))
