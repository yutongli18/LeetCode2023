"""
337.打家劫舍 III
其实叶子节点不需要单独考虑。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def post_traverse(self, node):
        # 节点状态：[不偷，偷]
        if not node:
            return [0, 0]
        left = self.post_traverse(node=node.left)
        right = self.post_traverse(node=node.right)
        val1 = max(left[0], left[1]) + max(right[0], right[1])
        val2 = left[0] + right[0] + node.val
        return [val1, val2]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val1, val2 = self.post_traverse(node=root)
        return max(val1, val2)
