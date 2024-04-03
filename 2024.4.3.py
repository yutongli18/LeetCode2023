"""
205. 同构字符串
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # start_list = [-1 for _ in range(256)]
        # end_list = [False for _ in range(256)]
        # for i in range(len(s)):
        #     start = ord(s[i])
        #     end = ord(t[i])
        #     if start_list[start] == -1:
        #         if end_list[end]:
        #             return False
        #         start_list[start] = end
        #         end_list[end] = True
        #     else:
        #         if end != start_list[start]:
        #             return False
        # return True
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            dict1.setdefault(s[i], t[i])
            dict2.setdefault(t[i], s[i])
            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]:
                return False
        print(dict1, dict2)
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic(s='paper', t='title'))
