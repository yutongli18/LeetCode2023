from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def level_order(self, root):
        if not root:
            return root
        queue = deque([root])
        while queue:
            pre_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if pre_node:
                    pre_node.next = node
                pre_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect(self, root):
        """
        116.填充每个节点的下一个右侧节点指针
        层序遍历。
        :type root: Node
        :rtype: Node
        """
        return self.level_order(root)
