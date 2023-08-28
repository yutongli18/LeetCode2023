"""
1047.删除字符串中的所有相邻重复项
用栈保存遍历过的元素
"""


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        sLength = len(s)
        for i in range(sLength):
            if len(stack) == 0 or stack[-1] != s[i]:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
        newS = "".join(stack)
        return newS


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates(s="abbaca"))
