# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.diameter = 0

    def getMaxDepth(self, node):
        """
        求以 node 为根节点的子树的最大深度（边数）。
        :param node: TreeNode
        :return: int
        """
        if not node:
            return -1
        left_depth = self.getMaxDepth(node.left)
        right_depth = self.getMaxDepth(node.right)
        # 每个根节点 node 都有可能在直径上，所以每个 node 都要算一次
        self.diameter = max(self.diameter, left_depth + right_depth + 2)
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root):
        """
        543.二叉树的直径
        :type root: TreeNode
        :rtype: int
        """
        self.getMaxDepth(root)
        return self.diameter
