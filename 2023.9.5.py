"""
199. 二叉树的右视图
其实就是层序遍历中每一层最右侧的节点
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        if root is None:
            return result_list
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            layer_list = []
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                layer_list.append(node.val)
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
            result_list.append(layer_list[-1])
        return result_list