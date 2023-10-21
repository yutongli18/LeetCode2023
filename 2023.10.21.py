class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildSubBST(self, nums):
        if not nums:
            return
        middle = int((len(nums) - 1) / 2)
        root = TreeNode(val=nums[middle])
        root.left = self.buildSubBST(nums[:middle])
        root.right = self.buildSubBST(nums[middle + 1:])
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildSubBST(nums)
