class Solution:
    def __init__(self):
        self.operations = ["+", "-", "*", "/"]

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in self.operations:
                op2, op1 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                else:
                    result = abs(op1) / abs(op2)
                    result = result * (-1) if op1 * op2 < 0 else result
                    stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
