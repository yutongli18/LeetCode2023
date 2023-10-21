class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.pre_node = None
        self.min_value = float("inf")

    def getSubMinimum(self, node):
        if not node:
            return
        self.getSubMinimum(node.left)
        if self.pre_node:
            difference = abs(node.val - self.pre_node.val)
            self.min_value = difference if difference < self.min_value else self.min_value
        self.pre_node = node
        self.getSubMinimum(node.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getSubMinimum(root)
        return self.min_value
