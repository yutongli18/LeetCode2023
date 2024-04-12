# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traverse(self, p, q):
        """
        比较以 p 为根节点的子树和以 q 为根节点的子树是否相同
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val:
            return False
        return self.traverse(p.left, q.left) and self.traverse(p.right, q.right)

    def isSameTree(self, p, q):
        """
        100.相同的树
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.traverse(p, q)
