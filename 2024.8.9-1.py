class Solution(object):
    def isValid(self, s):
        """
        20.有效的括号
        :type s: str
        :rtype: bool
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                if len(stack) > 0 and \
                        (s[i] == ")" and stack[-1] == "(" or
                         s[i] == "]" and stack[-1] == "[" or
                         s[i] == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            i += 1
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s="]"))
