# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inOrder(self, node):
        if not node:
            return []
        left_list = self.inOrder(node.left)
        right_list = self.inOrder(node.right)
        return left_list + [node.val] + right_list

    def kthSmallest(self, root, k):
        """
        230.二叉搜索树中第 K 小的元素
        中序遍历？中序遍历得到节点列表之后，返回第 (k-1) 个
        中序遍历
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inOrder(root)[k - 1]