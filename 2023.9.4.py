"""
107. 二叉树的层序遍历II
层序遍历 + 队列
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_list = []
        if root is None:
            return result_list
        queue = deque([root])
        while len(queue) > 0:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result_list.append(layer)
        result_list.reverse()
        return result_list