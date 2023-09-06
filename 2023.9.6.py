"""
637.二叉树的层平均值
本质上就是二叉树的层序遍历
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result_list = []
        if root is None:
            return result_list
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            layer_sum = 0
            layer_num = len(traverse_list)
            for _ in range(layer_num):
                node = traverse_list.popleft()
                layer_sum += node.val
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
            result_list.append(float(layer_sum) / layer_num)
        return result_list