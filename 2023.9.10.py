"""
117. 填充每个节点的下一个右侧节点指针II
因为用的是层序遍历的方法，所以无论是完全二叉树还是一般的二叉树都没有区别。
"""


from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        traverse_queue = deque([root])
        while len(traverse_queue) > 0:
            prev = None
            for _ in range(len(traverse_queue)):
                node = traverse_queue.popleft()
                if prev is not None:
                    prev.next = node
                prev = node
                if node.left is not None:
                    traverse_queue.append(node.left)
                if node.right is not None:
                    traverse_queue.append(node.right)
        return root
