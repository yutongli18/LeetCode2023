"""
654.最大二叉树
递归法。
和从前序+中序/后序+中序的思路是一样的，只不过现在需要自己寻找最大值作为数组的分割点。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructSubTree(vals):
    max_val, index = vals[0], 0
    for i in range(1, len(vals)):
        if vals[i] > max_val:
            max_val = vals[i]
            index = i
    root = TreeNode(val=max_val)
    left_vals = vals[:index]
    right_vals = vals[index + 1:]
    if len(left_vals) > 0:
        root.left = constructSubTree(left_vals)
    if len(right_vals) > 0:
        root.right = constructSubTree(right_vals)
    return root


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return constructSubTree(nums)
