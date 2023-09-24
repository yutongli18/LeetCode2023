"""
112. 路径总和
递归 + 回溯
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getPathSum(node, pathSum, targetSum):
    pathSum += node.val
    if node.left is None and node.right is None:
        if pathSum == targetSum:
            return True
        else:
            return False
    if node.left is not None and getPathSum(node.left, pathSum, targetSum):
        return True
    if node.right is not None and getPathSum(node.right, pathSum, targetSum):
        return True
    pathSum -= node.val
    return False


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        return getPathSum(root, 0, targetSum)