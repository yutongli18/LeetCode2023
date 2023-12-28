"""
337. 打家劫舍 III
在树上做动态规划。
后序遍历 + 动态规划。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def post_order(self, root):
        if not root:
            return [0, 0]
        if not root.left and not root.right:
            return [0, root.val]
        # 后序遍历
        left = self.post_order(root.left)
        right = self.post_order(root.right)
        # 偷当前节点
        val1 = root.val + left[0] + right[0]
        # 不偷当前节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])
        return [val2, val1]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.post_order(root=root)
        return max(result[0], result[1])
