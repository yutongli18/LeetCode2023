class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """def __init__(self):
        self.p_ancestors = []
        self.q_ancestors = []

    def getAncestors(self, node, ancestors, p, q):
        if not node:
            return
        ancestors.append(node)
        if node == p:
            self.p_ancestors = ancestors[:]
        if node == q:
            self.q_ancestors = ancestors[:]
        self.getAncestors(node.left, ancestors[:], p, q)
        self.getAncestors(node.right, ancestors[:], p, q)"""

    def getAncestors(self, node, p, q):
        if not node or node == p or node == q:
            return node
        left = self.getAncestors(node.left, p, q)
        right = self.getAncestors(node.right, p, q)
        if left and right:
            return node
        else:
            return left if left else right

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """self.getAncestors(root, [], p, q)
        common_ancestor = None
        left, right = 0, 0
        while left < len(self.p_ancestors) and right < len(self.q_ancestors):
            if self.p_ancestors[left] != self.q_ancestors[right]:
                break
            common_ancestor = self.p_ancestors[left]
            left += 1
            right += 1
        return common_ancestor"""
        return self.getAncestors(root, p, q)
