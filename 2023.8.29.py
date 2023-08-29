"""
150.逆波兰式求值
① 逆波兰式求值方法：遇到数字入栈，遇到运算符则将栈顶的两个元素运算后再入栈
② 在对负数做向零取整的操作（如 int，math.trunc 等）时，会出现问题（如 -3.5 会被取整到 -4），其实在代码随想录里也没有解决这个问题。
目前我想到的方法就是转换成正数先计算，再乘上符号
"""


from operator import add, sub, mul


class Solution(object):
    def __init__(self):
        self.ops = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            """if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                num2, num1 = stack.pop(), stack.pop()
                result = abs(num1) / abs(num2)
                stack.append(result * (-1) if num1 * num2 < 0 else result)
            else:
                stack.append(int(token))"""
            if token not in self.ops:
                stack.append(int(token))
            else:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(self.ops[token](op1, op2))
        return stack.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
