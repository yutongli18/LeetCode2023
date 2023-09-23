"""
513. 找树左下角的值
层序遍历比递归法更好理解。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        traverse_list = deque([root])
        layer_list = []
        while len(traverse_list) > 0:
            layer_list = []
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                layer_list.append(node.val)
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
        return layer_list[0]
