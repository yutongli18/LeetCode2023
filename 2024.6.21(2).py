from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        226.翻转二叉树
        层序遍历
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
