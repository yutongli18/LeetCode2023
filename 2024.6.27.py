# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        108.将有序数组转换为二叉搜索树
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0:
            return None
        start, end = 0, len(nums) - 1
        mid = (start + end) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
