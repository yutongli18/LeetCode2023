# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.traverse_list = []

    def inorder(self, node):
        if not node:
            return
        if node.left:
            self.inorder(node.left)
        self.traverse_list.append(node.val)
        if node.right:
            self.inorder(node.right)
        return

    def inorderTraversal(self, root):
        """
        94.二叉树的中序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.traverse_list
