# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_depth = 0
        self.depth = 0

    def preorder(self, node):
        """
        先序遍历求深度
        :param node: TreeNode
        :return: None
        """
        if not node:
            self.max_depth = max(self.max_depth, self.depth)
            return
        self.depth += 1
        self.preorder(node.left)
        self.preorder(node.right)
        self.depth -= 1
        return

    def get_depth(self, node, depth):
        """
        直接递归求最大深度
        :param node: TreeNode
        :param depth: int
        :return: int
        """
        if not node:
            return depth
        depth += 1
        left_depth = self.get_depth(node.left, depth)
        right_depth = self.get_depth(node.right, depth)
        depth -= 1
        return max(left_depth, right_depth)

    def maxDepth(self, root):
        """
        104.二叉树的最大深度
        先序遍历算深度
        :type root: TreeNode
        :rtype: int
        """
        return self.get_depth(root, 0)
