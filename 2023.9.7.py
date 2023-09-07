"""
429.N叉树的层序遍历
和二叉树的层序遍历同理
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
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
                if node.children is not None:
                    for children in node.children:
                        traverse_list.append(children)
            result_list.append(layer_list)
        return result_list
