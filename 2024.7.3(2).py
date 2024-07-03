# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.right_view = []

    def preOrder(self, node, level):
        if not node:
            return
        if level > len(self.right_view) - 1:
            self.right_view.append(node.val)
        self.preOrder(node.right, level + 1)
        self.preOrder(node.left, level + 1)
        return

    def rightSideView(self, root):
        """
        递归法
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preOrder(root, 0)
        return self.right_view
