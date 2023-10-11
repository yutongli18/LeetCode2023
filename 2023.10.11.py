"""
700. 二叉搜索树中的搜索
二叉搜索树本质上很像二分查找，但是没有数组那么有序。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchSubBST(node, val):
    if node is None:
        return
    if val == node.val:
        return node
    if val < node.val:
        return searchSubBST(node.left, val)
    else:
        return searchSubBST(node.right, val)


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return searchSubBST(root, val)
