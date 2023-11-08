"""
455. 分发饼干
贪心算法。
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        p1, p2 = 0, 0
        num_children = 0
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                num_children += 1
                p1 += 1
                p2 += 1
            elif s[p2] < g[p1]:
                p1 += 1
        return num_children


if __name__ == '__main__':
    sol = Solution()
    print(sol.findContentChildren(g=[1, 2], s=[1, 2, 3]))
