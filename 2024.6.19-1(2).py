# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        94.二叉树的中序遍历（迭代）
        在根节点上打标记
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        inorder_list = []
        stack = [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                inorder_list.append(stack.pop(-1).val)
        return inorder_list
