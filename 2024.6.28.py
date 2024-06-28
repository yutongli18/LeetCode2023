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
        self.inorder(node.left)
        self.traverse_list.append(node.val)
        self.inorder(node.right)
        return

    def isValidBST(self, root):
        """
        98.验证二叉搜索树
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        for i in range(1, len(self.traverse_list)):
            if self.traverse_list[i] <= self.traverse_list[i - 1]:
                return False
        return True
