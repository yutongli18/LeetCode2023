"""
二叉树的深度优先遍历
前/中/后序遍历
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(node, node_list):
    if node is None:
        return
    traverse(node=node.left, node_list=node_list)
    node_list.append(node.val)
    traverse(node=node.right, node_list=node_list)


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node_list = []
        traverse(node=root, node_list=node_list)
        return node_list
