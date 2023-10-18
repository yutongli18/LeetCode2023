"""
701.二叉搜索树中的插入操作
其实不需要重构树结构，直接插入叶子节点即可。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertSubBST(self, node, val):
        if val < node.val:
            if not node.left:
                new_node = TreeNode(val)
                node.left = new_node
                return
            else:
                self.insertSubBST(node.left, val)
        else:
            if not node.right:
                new_node = TreeNode(val)
                node.right = new_node
                return
            else:
                self.insertSubBST(node.right, val)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        self.insertSubBST(root, val)
        return root
