from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        102.二叉树的层序遍历
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        val_list = []
        if not root:
            return val_list
        queue = deque([root])
        while queue:
            curr_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            val_list.append(curr_list[:])
        return val_list
