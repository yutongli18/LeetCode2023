"""
515.在每个树行中找最大值
本质上是二叉树的层序遍历。
只要是问二叉树每一层如何如何的，都可以在层序遍历的基础上改进。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        if root is None:
            return result_list
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            layer_max = float("-inf")
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                layer_max = node if node.val > layer_max else layer_max
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
            result_list.append(layer_max)
        return result_list