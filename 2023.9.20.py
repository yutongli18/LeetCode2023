"""
100.相同的树
和对称的树代码相似，把比较对称位置上的节点改为比较相同位置上的节点即可
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkSame(node1, node2):
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
                return checkSame(node1.left, node2.left) and checkSame(node1.right, node2.right)


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return checkSame(p, q)
