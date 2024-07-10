# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_sum = -1001 * 3 * 10**4

    def checkMaxPath(self, node):
        if not node:
            return 0
        left_sum = self.checkMaxPath(node.left)
        right_sum = self.checkMaxPath(node.right)
        curr_sum = node.val + left_sum + right_sum
        self.max_sum = max(self.max_sum, curr_sum, node.val, node.val + left_sum, node.val + right_sum)
        return max(node.val, node.val + left_sum, node.val + right_sum)

    def maxPathSum(self, root):
        """
        124.二叉树中的最大路径和
        :type root: TreeNode
        :rtype: int
        """
        self.checkMaxPath(root)
        return self.max_sum
