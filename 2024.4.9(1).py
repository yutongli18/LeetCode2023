class Solution(object):
    def process_string(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '#':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(s[i])
        return ''.join(stack)

    def backspaceCompare(self, s, t):
        """
        844. 比较含退格的字符串
        栈解法（空间复杂度 O(n)）
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.process_string(s) == self.process_string(t)


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare(s="ab#c", t='ad#c'))
