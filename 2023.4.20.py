class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackList = []  # 栈
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stackList.append(char)
            elif char == ")":
                if len(stackList) > 0 and stackList[-1] == "(":
                    stackList.pop(-1)
                else:
                    return False
            elif char == "}":
                if len(stackList) > 0 and stackList[-1] == "{":
                    stackList.pop(-1)
                else:
                    return False
            else:
                if len(stackList) > 0 and stackList[-1] == "[":
                    stackList.pop(-1)
                else:
                    return False
        if len(stackList) > 0:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(s="()"))
