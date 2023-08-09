"""
20.有效的括号
一个小技巧：在找到左括号时，让对应的右括号入栈。在匹配到右括号时，直接比对右括号和栈顶元素是否相等，效果更好。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """valid_list = []
        for char in s:
            if char in ["(", "{", "["]:
                valid_list.append(char)
            else:
                if len(valid_list) == 0:
                    return False
                else:
                    prev = valid_list.pop()
                    if char == ")":
                        if prev != "(":
                            return False
                    elif char == "]":
                        if prev != "[":
                            return False
                    else:
                        if prev != "{":
                            return False
        if len(valid_list) != 0:
            return False
        return True"""
        valid_list = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char == "(":
                valid_list.append(")")
            elif char == "[":
                valid_list.append("]")
            elif char == "{":
                valid_list.append("}")
            else:
                if len(valid_list) == 0:
                    return False
                else:
                    prev = valid_list.pop()
                    if prev != char:
                        return False
        if len(valid_list) != 0:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(s="(]"))
