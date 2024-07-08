class Solution(object):
    def reverse_list(self, s_list):
        """
        翻转列表
        :param s_list: list[int]
        :return: list[int]
        """
        left, right = 0, len(s_list) - 1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return s_list

    def getEncryptedString(self, s, k):
        """
        100339.找出加密后的字符串
        循环右移
        :type s: str
        :type k: int
        :rtype: str
        """
        s_length = len(s)
        # 右移的位数
        step = s_length - (k % s_length)
        # 右移：先整体翻转再局部翻转
        s_list = list(s)
        s_list.reverse()
        new_list = self.reverse_list(s_list[:step])
        new_list.extend(self.reverse_list(s_list[step:]))
        return ''.join(new_list)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getEncryptedString(s="dart", k=6))
