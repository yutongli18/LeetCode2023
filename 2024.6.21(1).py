# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invert(self, node):
        """
        递归地翻转当前节点
        :param node: TreeNode
        :return: TreeNode
        """
        if not node:
            return node
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        self.invert(node.left)
        self.invert(node.right)
        return node

    def invertTree(self, root):
        """
        226.翻转二叉树
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
