class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkSymmetric(node1, node2):
    if node1 is None:
        if node2 is None:
            return True
        else:
            return False
    else:
        if node2 is None:
            return False
        else:
            if node1.val != node2.val:
                return False
            else:
                return checkSymmetric(node1.left, node2.right) and checkSymmetric(node1.right, node2.left)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return checkSymmetric(root.left, root.right)
