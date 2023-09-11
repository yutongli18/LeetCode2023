"""
104.二叉树的最大深度
因为是和二叉树的层有关的，也可以用层序遍历解决。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num_layers = 0
        if root is None:
            return num_layers
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
            num_layers += 1
        return num_layers
