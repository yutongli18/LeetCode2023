"""
225.用队列实现栈
可以只用一个队列实现栈，在出队列的同时在末尾入队列，直到弹出最后一个元素为止
"""


from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            return None
        length = len(self.queue)
        for _ in range(length - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        stack_top = self.pop()
        self.queue.append(stack_top)
        return stack_top

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False
