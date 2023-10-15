class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMaxDepth(node, max_depth):
    if not node:
        return max_depth
    max_depth += 1
    return max(getMaxDepth(node.left, max_depth), getMaxDepth(node.right, max_depth))


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return getMaxDepth(root, 0)
