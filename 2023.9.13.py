"""
226.翻转二叉树
最先想到的是层序遍历，但是其实深度优先遍历也可以实现。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """if root is None:
            return root
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            node = traverse_list.popleft()
            curr_left, curr_right = node.left, node.right
            node.left = curr_right
            node.right = curr_left
            if node.left is not None:
                traverse_list.append(node.left)
            if node.right is not None:
                traverse_list.append(node.right)
        return root"""
        # 前序遍历
        if root is None:
            return root
        traverse_list = [root]
        while len(traverse_list) > 0:
            node = traverse_list.pop()
            if node is not None:
                curr_left, curr_right = node.left, node.right
                node.left, node.right = curr_right, curr_left
                if node.right is not None:
                    traverse_list.append(node.right)
                if node.left is not None:
                    traverse_list.append(node.left)
                traverse_list.append(node)
                traverse_list.append(None)
            else:
                traverse_list.pop()
        return root