# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.sort_list = []

    def inorder(self, node):
        """
        中序遍历
        :type node: TreeNode
        :rtype: None
        """
        if not node:
            return
        if node.left:
            self.inorder(node.left)
        self.sort_list.append(node.val)
        if node.right:
            self.inorder(node.right)
        return

    def construct(self, start, end):
        """
        从有序数组构建平衡二叉搜索树
        :type start: int
        :type end: int
        :rtype: TreeNode
        """
        if start > end:
            return
        mid = int((start + end) / 2)
        root = TreeNode(val=self.sort_list[mid])
        root.left = self.construct(start=start, end=mid - 1)
        root.right = self.construct(start=mid + 1, end=end)
        return root

    def balanceBST(self, root):
        """
        1382.将二叉搜索树变平衡
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder(node=root)
        return self.construct(start=0, end=len(self.sort_list) - 1)
