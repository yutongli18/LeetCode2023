from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        101.对称二叉树
        迭代
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root.left, root.right])
        while queue:
            left_node = queue.popleft()
            right_node = queue.popleft()
            if not left_node and not right_node:
                continue
            if (not left_node and right_node) or (left_node and not right_node) or (left_node.val != right_node.val):
                return False
            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)
        return True
