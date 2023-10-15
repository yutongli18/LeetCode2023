class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinDepth(node, min_depth):
    min_depth += 1
    if not node.left:
        if not node.right:
            return min_depth
        else:
            return getMinDepth(node.right, min_depth)
    else:
        if not node.right:
            return getMinDepth(node.left, min_depth)
        else:
            return min(getMinDepth(node.left, min_depth), getMinDepth(node.right, min_depth))


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return getMinDepth(root, 10 ** 5 + 1)
