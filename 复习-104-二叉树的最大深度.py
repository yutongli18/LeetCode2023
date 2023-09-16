class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMaxDepth(node, depth):
    """
    其实二叉树最大最小深度的递归方法逻辑是一样的，只是把最大值换成最小值而已。
    注意对于二叉树的最小深度，不能直接把左子树的 depth 赋值为当前的 depth，必须顺着另一个不为空的子节点去查找。
    """
    if node is None:
        return depth
    depth += 1
    left_depth = getMaxDepth(node.left, depth) if node.left is not None else depth
    right_depth = getMaxDepth(node.right, depth) if node.right is not None else depth
    return max(left_depth, right_depth)


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return getMaxDepth(root, 0)