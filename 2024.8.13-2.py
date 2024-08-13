class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_value = 0

    def push(self, val):
        if len(self.stack) <= 0:
            self.min_value = val
        self.stack.append(val - self.min_value)
        self.min_value = min(self.min_value, val)

    def pop(self):
        if self.stack[-1] <= 0:
            # 说明当前栈顶就是最小的元素，其值在self.min_value中保存着
            # 弹栈顶的话要修改保存的最小值
            self.min_value = self.min_value - self.stack.pop()
        else:
            self.stack.pop()

    def top(self):
        if self.stack[-1] < 0:
            return self.min_value
        else:
            return self.stack[-1] + self.min_value

    def getMin(self):
        return self.min_value


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
