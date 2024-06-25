# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def checkSymmetric(self, left, right):
        """
        判断两棵子树是否对称
        :param left: TreeNode
        :param right: TreeNode
        :return: Boolean
        """
        if not left:
            if right:
                return False
            else:
                return True
        else:
            if not right:
                return False
            else:
                if left.val != right.val:
                    return False
        return left.val == right.val and self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right,
                                                                                                             right.left)

    def isSymmetric(self, root):
        """
        101.对称二叉树
        递归
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSymmetric(root.left, root.right)
