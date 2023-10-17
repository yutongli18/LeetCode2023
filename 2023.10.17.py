"""
235.二叉搜索树的最近公共祖先
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getCommonAncestor(self, node, p, q):
        # p.val < q.val
        if node == p or node == q or p.val < node.val < q.val:
            return node
        if node.val > q.val:
            return self.getCommonAncestor(node.left, p, q)
        if node.val < p.val:
            return self.getCommonAncestor(node.right, p, q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        return self.getCommonAncestor(root, p, q)
