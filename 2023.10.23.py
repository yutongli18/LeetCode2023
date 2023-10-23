"""
538. 把二叉搜索树转换为累加树
右中左遍历，找后缀和即可。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.cum_sum = 0

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.right)
        node.val += self.cum_sum
        self.cum_sum = node.val
        self.traverse(node.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root)
        return root
