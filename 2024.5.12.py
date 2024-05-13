class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        100296.两个字符串的排列差
        :type s: str
        :type t: str
        :rtype: int
        """
        a_code = ord('a')
        # 字母位置
        pos = [-1 for _ in range(26)]
        # 指向两个字符串的指针
        ptr1, ptr2 = 0, 0
        # 排列差
        diff_count = 0
        while ptr1 < len(s):
            if s[ptr1] != t[ptr2]:
                if pos[ord(s[ptr1]) - a_code] != -1:
                    diff_count += abs(pos[ord(s[ptr1]) - a_code] - ptr1)
                    pos[ord(s[ptr1]) - a_code] = -1
                else:
                    pos[ord(s[ptr1]) - a_code] = ptr1
                if pos[ord(t[ptr2]) - a_code] != -1:
                    diff_count += abs(pos[ord(t[ptr2]) - a_code] - ptr2)
                    pos[ord(t[ptr2]) - a_code] = -1
                else:
                    pos[ord(t[ptr2]) - a_code] = ptr2
            ptr1 += 1
            ptr2 += 1
        return diff_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPermutationDifference(s="abcde", t="edbac"))
