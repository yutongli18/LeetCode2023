class Solution(object):
    def getSmallestString(self, s):
        """
        100352.交换后字典序最小的字符串
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        left, right = 0, 1
        while right < len(s_list):
            if int(s_list[left]) % 2 == int(s_list[right]) % 2 and int(s_list[left]) > int(s_list[right]):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                break
            left += 1
            right += 1
        return "".join(s_list)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSmallestString("001"))
