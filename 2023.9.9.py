"""
116.填充每个节点的下一个右侧指针
本质是二叉树的层序遍历。
每次要更新 prev 指针指向前一个节点。
"""


from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            prev = None
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                if prev is not None:
                    prev.next = node
                prev = node
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
        return root