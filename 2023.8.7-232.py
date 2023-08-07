"""
232.用栈实现队列
输入栈和输出栈
注意：不要求在操作之后内部的数据结构符合一条队列的数据结构。换言之，两个栈中可以都有元素。
"""


class MyQueue(object):

    def __init__(self):
        """self.stack_1 = []
        self.stack_2 = []"""
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        """self.stack_1.append(x)"""
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        """while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())
        item = self.stack_2.pop()
        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())
        return item"""
        # 这里：如果输出栈不为空，则一定直接弹出输出栈的栈顶，因为输出栈中的元素入栈的时间一定早于输入栈中的元素
        # 输出栈中剩余的元素是之前在出队列操作中从输入栈移动过来的
        if self.empty():
            return None
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        item = self.pop()
        self.stack_out.append(item)
        return item

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        return False
