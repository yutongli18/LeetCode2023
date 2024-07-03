from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        199.二叉树的右视图
        层序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        right_view = []
        if not root:
            return right_view
        queue = deque([root])
        while queue:
            curr_length = len(queue)
            i = 0
            while i < curr_length:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == curr_length - 1:
                    right_view.append(node.val)
                i += 1
        return right_view
