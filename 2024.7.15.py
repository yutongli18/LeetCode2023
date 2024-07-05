# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        105.从前序与中序遍历序列构造二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) <= 0 or len(inorder) <= 0:
            return
        root = TreeNode(val=preorder[0])
        split = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:split + 1], inorder[:split])
        root.right = self.buildTree(preorder[split + 1:], inorder[split + 1:])
        return root
