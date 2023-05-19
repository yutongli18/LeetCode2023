"""
1026.节点与其祖先之间的最大差值
在遍历一次二叉树的同时，寻找当前的最大/小祖先节点，同时找到子节点，使差值最大。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, minPre, maxPre):
            if root is None:
                return 0
            diff = max(abs(root.val - minPre), abs(root.val - maxPre))
            minPre = min(root.val, minPre)
            maxPre = max(root.val, maxPre)
            diff = max(diff, dfs(root.left, minPre, maxPre))
            diff = max(diff, dfs(root.right, minPre, maxPre))
            return diff
        return dfs(root, root.val, root.val)
