class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def preorder(self, node):
        if not node:
            return
        if node.left and node.right:
            # 先连接两个子节点
            node.left.next = node.right
        if node.right and node.next:
            node.right.next = node.next.left
        self.preorder(node.left)
        self.preorder(node.right)

    def connect(self, root):
        """
        116. 填充每个节点的下一个右侧节点指针
        先序遍历（递归）
        :type root: Node
        :rtype: Node
        """
        self.preorder(root)
        return root
