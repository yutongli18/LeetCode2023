class Solution(object):
    def clearStars(self, s):
        """
        100322.删除星号以后字典序最小的字符串
        :type s: str
        :rtype: str
        """
        a_code = ord('a')
        char_dict = [[] for _ in range(26)]
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == "*":
                for j in range(26):
                    if char_dict[j]:
                        index = char_dict[j].pop(-1)
                        s_list[index] = "*"
                        break
            else:
                char_dict[ord(s_list[i]) - a_code].append(i)
        new_s = ""
        for i in range(len(s_list)):
            if s_list[i] != "*":
                new_s += s_list[i]
        return new_s


if __name__ == "__main__":
    sol = Solution()
    print(sol.clearStars(s="d*o*"))
